#!/usr/bin/env python

import os
import re


def rename_in_bulk(files, pattern=r"[^(]*\(([0-9]+)\).*", replace=r"\1"):
    for source in files:
        target = re.sub(pattern, replace, source)
        os.rename(source, target)


def test_pattern():
    assert re.sub(r"[^(]*\(([0-9]+)\).*", r"\1", "a(1000).txt") == "1000"
    assert re.sub(r"[^(]*\(([0-9]+)\).*", r"\1", "a1000.txt") == "a1000.txt" # File that doesn't match is skipped


def test_execution():
    from unittest.mock import patch

    expected = [(("a (0).txt", "0"),), (("a(1000).txt", "1000"),)]
    files = [it[0][0] for it in expected]

    with patch("os.rename") as rename:
        rename_in_bulk(files)
        assert rename.call_args_list == expected


def path2files(path):
    return [f for f in os.listdir(path) if os.path.isfile(f)]


def main(args):
    files = path2files(args.path2files)
    rename_in_bulk(files, args.pattern, args.replace)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Renames files in bulk")
    parser.add_argument(
        "path2files",
        type=str,
        default=os.curdir,
        help="points where the files to be renamed are located",
    )
    parser.add_argument(
        "--pattern",
        type=str,
        default=r"[^(]*\(([0-9]+)\).*",
        help="defines the matching pattern for the original file names (default: '%(default)s')",
    )
    parser.add_argument(
        "--replace",
        type=str,
        default=r"\1",
        help="defines the substitution pattern from the original file names to the target ones (default: '%(default)s')",
    )

    args = parser.parse_args()
    main(args)
