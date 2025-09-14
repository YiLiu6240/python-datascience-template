#!/usr/bin/env python3
"""
Hello World Data Science Script

A simple example script demonstrating basic data science practices.
Run with: python scripts/hello_world.py
"""

import argparse

from local_funcs import example_data_processing_function, hello


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Parsed command-line arguments
    """
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # ---- --numbers ----
    parser.add_argument(
        "--numbers",
        type=int,
        nargs="+",
        default=[1, 2, 3, 4, 5],
        help="Numbers to process (default: 1 2 3 4 5)",
    )

    # ---- --dry-run ----
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Show what would be done without executing",
    )

    return parser.parse_args()


def main() -> None:
    """Main function to demonstrate data science workflow."""
    args = parse_args()

    print(hello())
    print(f"Input numbers: {args.numbers}")

    if args.dry_run:
        print("DRY RUN: Would process the numbers but not executing")
        return

    # ---- Process data ----
    processed_data = example_data_processing_function(args.numbers)
    print(f"Processed numbers: {processed_data}")

    # ---- Basic statistics ----
    original_sum = sum(args.numbers)
    processed_sum = sum(processed_data)

    print(f"Original sum: {original_sum}")
    print(f"Processed sum: {processed_sum}")
    print(f"Ratio: {processed_sum / original_sum:.2f}")


if __name__ == "__main__":
    main()
