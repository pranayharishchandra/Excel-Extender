"""Data structures and models for application state."""

from dataclasses import dataclass
from typing import List

@dataclass
class SheetConfig:
    sheet_name: str
    template_start_row: int
    rows_per_material: int
    managed_columns: List[int]
    preserve_existing: bool