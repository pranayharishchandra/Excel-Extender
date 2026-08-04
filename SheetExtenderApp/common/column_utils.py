"""
common/column_utils.py

Utility functions for working with Excel column letters and indexes.

These helpers wrap openpyxl's utilities to provide consistent validation
and conversion throughout the application.
"""

from __future__ import annotations

from typing import Iterable, List

from openpyxl.utils import (
    column_index_from_string,
    get_column_letter,
)


def normalize_column_letter(column: str) -> str:
    """
    Normalize and validate an Excel column letter.

    Args:
        column:
            Excel column letter.

    Returns:
        Uppercase Excel column letter.

    Raises:
        ValueError:
            If the column is empty or invalid.
    """
    if column is None:
        raise ValueError("Column cannot be None.")

    column = str(column).strip().upper()

    if not column:
        raise ValueError("Column cannot be empty.")

    try:
        column_index_from_string(column)
    except ValueError as exc:
        raise ValueError(f"Invalid Excel column '{column}'.") from exc

    return column


def column_letter_to_index(column: str) -> int:
    """
    Convert an Excel column letter to a 1-based column index.

    Args:
        column:
            Excel column letter.

    Returns:
        1-based column index.
    """
    return column_index_from_string(normalize_column_letter(column))


def column_index_to_letter(index: int) -> str:
    """
    Convert a 1-based column index to an Excel column letter.

    Args:
        index:
            1-based column index.

    Returns:
        Excel column letter.

    Raises:
        ValueError:
            If the index is invalid.
    """
    if index < 1:
        raise ValueError("Column index must be greater than zero.")

    return get_column_letter(index)


def normalize_column_list(columns: Iterable[str]) -> List[str]:
    """
    Normalize a collection of Excel column letters.

    Invalid columns raise ValueError.

    Duplicate columns are removed while preserving order.

    Args:
        columns:
            Iterable of Excel column letters.

    Returns:
        List of normalized column letters.
    """
    normalized: List[str] = []
    seen: set[str] = set()

    for column in columns:
        letter = normalize_column_letter(column)

        if letter not in seen:
            normalized.append(letter)
            seen.add(letter)

    return normalized


def parse_managed_columns(value: str, separator: str = ",") -> List[str]:
    """
    Parse the Managed Columns configuration value.

    Example:
        "B,D,E,G"
            ->
        ["B", "D", "E", "G"]

    Args:
        value:
            Raw configuration cell value.

        separator:
            Column separator.

    Returns:
        List of normalized Excel column letters.
    """
    if value is None:
        return []

    value = str(value).strip()

    if not value:
        return []

    parts = [part.strip() for part in value.split(separator)]

    return normalize_column_list(parts)


def is_valid_column(column: str) -> bool:
    """
    Returns whether a value is a valid Excel column letter.

    Args:
        column:
            Excel column letter.

    Returns:
        True if valid, otherwise False.
    """
    try:
        normalize_column_letter(column)
        return True
    except ValueError:
        return False


def sort_columns(columns: Iterable[str]) -> List[str]:
    """
    Sort Excel column letters into worksheet order.

    Example:
        ["AA", "A", "C", "B"]
            ->
        ["A", "B", "C", "AA"]

    Args:
        columns:
            Collection of Excel column letters.

    Returns:
        Sorted list of normalized column letters.
    """
    normalized = normalize_column_list(columns)

    return sorted(
        normalized,
        key=column_letter_to_index,
    )