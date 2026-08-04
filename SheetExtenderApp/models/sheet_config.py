# Step 1: Because everything depends on this file

"""
Dataclasses used throughout the Excel Formula Extension Engine.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class SheetConfig:
    """
    Represents one worksheet configuration read from the
    'pranay_extension_config' sheet.
    """

    sheet_name: str
    template_start_row: int
    rows_per_material: int
    managed_columns: List[int]
    preserve_existing: bool


@dataclass(slots=True)
class WorkbookInfo:
    """
    Stores workbook-related information discovered at runtime.
    """

    workbook_path: str
    previous_material_count: int
    new_material_count: int


@dataclass(slots=True)
class ProcessingResult:
    """
    Result of processing a single worksheet.
    """

    sheet_name: str
    success: bool
    message: str


@dataclass(slots=True)
class ValidationResult:
    """
    Stores configuration validation results.
    """

    is_valid: bool = True
    errors: List[str] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        self.is_valid = False
        self.errors.append(message)