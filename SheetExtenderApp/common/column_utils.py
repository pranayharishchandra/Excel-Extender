# Column conversions
# Everything related to Excel columns lives in one place.

"""
Utility functions for working with Excel columns.

Examples
--------
"B"         -> 2
"AA"        -> 27
"B,C,D,G"   -> [2,3,4,7]
[2,3,4,7]   -> ["B","C","D","G"]
"""

from __future__ import annotations

from typing import List

from openpyxl.utils import (
    column_index_from_string,
    get_column_letter,
)


def column_letter_to_index(column: str) -> int:
    """
    Convert an Excel column letter to a 1-based column index.

    Example
    -------
    "A" -> 1
    "B" -> 2
    "AA" -> 27
    """
    return column_index_from_string(column.strip().upper())


def column_index_to_letter(index: int) -> str:
    """
    Convert a 1-based column index into an Excel column letter.

    Example
    -------
    1 -> "A"
    2 -> "B"
    27 -> "AA"
    """
    return get_column_letter(index)


def parse_managed_columns(columns: str) -> List[int]:
    """
    Convert a comma-separated column string into a sorted list
    of unique column indexes.

    Example
    -------
    "B,C,D,G"

    returns

    [2,3,4,7]
    """

    if not columns.strip():
        return []

    parsed = {
        column_letter_to_index(col)
        for col in columns.split(",")
        if col.strip()
    }

    return sorted(parsed)


def managed_columns_to_string(columns: List[int]) -> str:
    """
    Convert column indexes back into a comma-separated string.

    Example
    -------
    [2,3,4]

    returns

    "B,C,D"
    """

    return ",".join(
        column_index_to_letter(col)
        for col in sorted(columns)
    )


def is_valid_column(column: str) -> bool:
    """
    Returns True if the supplied Excel column is valid.

    Example
    -------
    "A"      -> True
    "AB"     -> True
    "123"    -> False
    "A1"     -> False
    """

    try:
        column_letter_to_index(column)
        return True
    except ValueError:
        return False


def validate_managed_columns(columns: str) -> List[str]:
    """
    Validate a managed column string.

    Returns a list of validation errors.
    Empty list means valid.
    """

    errors: List[str] = []

    if not columns.strip():
        errors.append("Managed Columns cannot be empty.")
        return errors

    for column in columns.split(","):

        column = column.strip()

        if not column:
            continue

        if not is_valid_column(column):
            errors.append(f"Invalid column '{column}'.")

    return errors