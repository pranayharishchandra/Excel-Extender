"""
common/excel_headers.py

Definitions for configuration worksheet headers.

The configuration worksheet is parsed by header names rather than fixed
column positions. This module centralizes those header names and provides
helper utilities for validating and locating them.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable

from .constants import (
    HEADER_MANAGED_COLUMNS,
    HEADER_PRESERVE_EXISTING,
    HEADER_ROWS_PER_MATERIAL,
    HEADER_SHEET_NAME,
    HEADER_TEMPLATE_START_ROW,
)


@dataclass(frozen=True, slots=True)
class ConfigHeaders:
    """
    Canonical names of the required configuration worksheet headers.
    """

    sheet_name: str = HEADER_SHEET_NAME
    template_start_row: str = HEADER_TEMPLATE_START_ROW
    rows_per_material: str = HEADER_ROWS_PER_MATERIAL
    managed_columns: str = HEADER_MANAGED_COLUMNS
    preserve_existing: str = HEADER_PRESERVE_EXISTING

    @property
    def required(self) -> tuple[str, ...]:
        """
        Returns all required configuration headers.
        """
        return (
            self.sheet_name,
            self.template_start_row,
            self.rows_per_material,
            self.managed_columns,
            self.preserve_existing,
        )


HEADERS = ConfigHeaders()


def normalize_header(header: str) -> str:
    """
    Normalize a header for case-insensitive comparison.

    Leading/trailing whitespace is removed and consecutive whitespace
    is collapsed into a single space.

    Args:
        header:
            Raw header text.

    Returns:
        Normalized header string.
    """
    if header is None:
        return ""

    return " ".join(str(header).strip().split()).casefold()


def build_header_map(headers: Iterable[str]) -> Dict[str, int]:
    """
    Build a normalized header-to-column-index mapping.

    Column indexes are 1-based to match openpyxl.

    Args:
        headers:
            Header values from the worksheet.

    Returns:
        Dictionary mapping normalized header names to column indexes.

    Raises:
        ValueError:
            If duplicate header names are encountered.
    """
    mapping: Dict[str, int] = {}

    for index, header in enumerate(headers, start=1):
        normalized = normalize_header(header)

        if not normalized:
            continue

        if normalized in mapping:
            raise ValueError(f"Duplicate configuration header: '{header}'.")

        mapping[normalized] = index

    return mapping


def missing_required_headers(
    header_map: Dict[str, int],
) -> list[str]:
    """
    Determine which required headers are missing.

    Args:
        header_map:
            Mapping produced by ``build_header_map``.

    Returns:
        List of missing required header names.
    """
    missing: list[str] = []

    for header in HEADERS.required:
        if normalize_header(header) not in header_map:
            missing.append(header)

    return missing


def has_all_required_headers(header_map: Dict[str, int]) -> bool:
    """
    Returns whether all required headers are present.

    Args:
        header_map:
            Mapping produced by ``build_header_map``.

    Returns:
        True if every required header exists; otherwise False.
    """
    return not missing_required_headers(header_map)


def get_header_column(
    header_map: Dict[str, int],
    header_name: str,
) -> int:
    """
    Retrieve the 1-based column index for a configuration header.

    Args:
        header_map:
            Mapping produced by ``build_header_map``.

        header_name:
            Canonical header name.

    Returns:
        1-based Excel column index.

    Raises:
        KeyError:
            If the header is not present.
    """
    normalized = normalize_header(header_name)

    try:
        return header_map[normalized]
    except KeyError as exc:
        raise KeyError(
            f"Configuration header '{header_name}' was not found."
        ) from exc