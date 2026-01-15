#!/usr/bin/env python3
"""
2-1.py

Usage:
    python3 2-1.py <path-to-input-file>

The input file contains lines with one or more numeric ranges separated by commas.
Each range is expressed as "start-end" (inclusive). The script finds all *invalid IDs*
within those ranges and prints the sum of those IDs.

An *invalid ID* is a positive integer whose decimal representation consists of a
non‑empty sequence of digits repeated exactly twice. Examples:
    55      -> "5" repeated twice
    6464    -> "64" repeated twice
    123123  -> "123" repeated twice

The algorithm:
    1. Parse all ranges and determine the maximum upper bound.
    2. Generate every number that matches the "double‑repeat" pattern up to that bound.
    3. For each range, add the generated numbers that fall inside the range.
    4. Output the total sum.
"""

import sys
import os
from typing import List, Tuple


def parse_ranges(file_path: str) -> List[Tuple[int, int]]:
    """
    Read the file and return a list of (start, end) integer tuples.
    Empty lines are ignored. Whitespace around tokens is stripped.
    """
    ranges = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Split by commas – each token should be a range like "12-34"
            for token in line.split(","):
                token = token.strip()
                if not token:
                    continue
                if "-" not in token:
                    raise ValueError(f"Invalid range token '{token}' (missing '-')")
                start_str, end_str = token.split("-", 1)
                start = int(start_str.strip())
                end = int(end_str.strip())
                if start > end:
                    raise ValueError(f"Range start {start} greater than end {end}")
                ranges.append((start, end))
    return ranges


def generate_invalid_ids(limit: int) -> List[int]:
    """
    Generate all numbers <= limit whose decimal representation is a
    non‑empty string repeated twice (e.g., 55, 6464, 123123).
    """
    invalid_ids = []
    # The length of the full number cannot exceed len(str(limit))
    max_len = len(str(limit))
    # Full length must be even, so half length ranges from 1 to max_len // 2
    for half_len in range(1, max_len // 2 + 1):
        # The first digit of the half cannot be zero (no leading zeros in the final number)
        start_half = 10 ** (half_len - 1)
        end_half = 10 ** half_len - 1
        for half in range(start_half, end_half + 1):
            s = str(half)
            candidate = int(s + s)  # repeat the half string
            if candidate > limit:
                # Since halves are increasing, we can break early for this half_len
                break
            invalid_ids.append(candidate)
    return invalid_ids


def sum_invalid_ids_in_ranges(ranges: List[Tuple[int, int]], invalid_ids: List[int]) -> int:
    """
    Given a list of ranges and a pre‑computed sorted list of invalid IDs,
    compute the sum of all invalid IDs that fall inside any of the ranges.
    """
    total = 0
    # Ensure the list is sorted for efficient scanning
    invalid_ids.sort()
    idx = 0
    n = len(invalid_ids)

    # Process each range in ascending order of start to keep the scan linear
    for start, end in sorted(ranges, key=lambda x: x[0]):
        # Advance idx to the first candidate >= start
        while idx < n and invalid_ids[idx] < start:
            idx += 1
        # Add all candidates <= end
        j = idx
        while j < n and invalid_ids[j] <= end:
            total += invalid_ids[j]
            j += 1
        # Keep idx where we left off for the next range (ranges are sorted)
        idx = j
    return total


def main() -> None:
    if len(sys.argv) != 2:
        prog = os.path.basename(sys.argv[0])
        print(f"Usage: python3 {prog} <input-file>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    try:
        ranges = parse_ranges(input_path)
    except Exception as e:
        print(f"Error parsing input file: {e}", file=sys.stderr)
        sys.exit(1)

    if not ranges:
        print(0)
        return

    max_upper = max(end for _, end in ranges)
    invalid_ids = generate_invalid_ids(max_upper)
    total = sum_invalid_ids_in_ranges(ranges, invalid_ids)
    print(total)


if __name__ == "__main__":
    main()
