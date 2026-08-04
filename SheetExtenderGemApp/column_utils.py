"""Utility functions for handling Excel columns."""

from openpyxl.utils import column_index_from_string
from typing import List

def parse_managed_columns(col_string: str) -> List[int]:
    """
    Parses a comma-separated string of column letters into a list of 1-based column indices.
    Example: 'B,C,D' -> [2, 3, 4]
    """
    if not col_string:
        return []
    
    # Strip whitespace, convert to uppercase, and drop empty entries
    cols = [c.strip().upper() for c in col_string.split(',') if c.strip()]
    return [column_index_from_string(c) for c in cols]