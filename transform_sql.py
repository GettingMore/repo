#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List


SWIFT_BLOCK_RE = re.compile(
    r"(?is)\bswift\b.*?(?:\bend\s+swift\b|\bend\s*swift\b|$)"
)
CURSOR_DECLARE_RE = re.compile(r"(?is)\bcursor\s+declare\s+(\w+)\s+for\b")
SELECT_INTO_RE = re.compile(r"(?is)\bselect\b(.*?)\binto\b(.*?)\bfrom\b")


def split_csv(fragment: str) -> List[str]:
    items: List[str] = []
    buffer: List[str] = []
    depth = 0
    in_single = False
    in_double = False
    for char in fragment:
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "(" and not in_single and not in_double:
            depth += 1
        elif char == ")" and not in_single and not in_double and depth > 0:
            depth -= 1

        if char == "," and depth == 0 and not in_single and not in_double:
            items.append("".join(buffer).strip())
            buffer = []
        else:
            buffer.append(char)

    tail = "".join(buffer).strip()
    if tail:
        items.append(tail)
    return items


def transform_swift_blocks(sql: str) -> str:
    def _replace(match: re.Match) -> str:
        content = match.group(0).strip()
        return f"/* SWIFT_BLOCK {content} */"

    return SWIFT_BLOCK_RE.sub(_replace, sql)


def transform_cursor_declare(sql: str) -> str:
    def _replace(match: re.Match) -> str:
        cursor_name = match.group(1)
        return f"/* CURSOR DECLARE {cursor_name} */"

    return CURSOR_DECLARE_RE.sub(_replace, sql)


def transform_select_into(sql: str) -> str:
    def _replace(match: re.Match) -> str:
        select_list = match.group(1)
        into_list = match.group(2)
        select_items = split_csv(select_list)
        into_items = [item.strip().lstrip(":") for item in split_csv(into_list)]

        if len(select_items) == len(into_items) and select_items:
            aliased = [
                f"{col.strip()} AS {var}" for col, var in zip(select_items, into_items)
            ]
            return f"SELECT {', '.join(aliased)} FROM"

        fallback = re.sub(r":(\w+)", r"\1", into_list)
        return f"SELECT {select_list} AS {fallback} FROM"

    return SELECT_INTO_RE.sub(_replace, sql)


def transform_sql(sql: str) -> str:
    sql = transform_swift_blocks(sql)
    sql = transform_cursor_declare(sql)
    sql = transform_select_into(sql)
    return sql


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Transform PROC SQL to MyBatis-friendly SQL by "
            "commenting SWIFT blocks, rewriting CURSOR DECLARE, "
            "and converting SELECT ... INTO :vars to SELECT ... AS vars."
        )
    )
    parser.add_argument("file", nargs="?", help="Input SQL file. Reads stdin if omitted.")
    args = parser.parse_args()

    if args.file:
        sql = Path(args.file).read_text(encoding="utf-8")
    else:
        sql = sys.stdin.read()

    sys.stdout.write(transform_sql(sql))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
