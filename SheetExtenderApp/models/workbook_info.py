"""
models/workbook_info.py

Model representing the currently loaded Excel workbook and
its associated metadata.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List


@dataclass(slots=True)
class WorkbookInfo:
    """
    Stores metadata about the selected workbook.

    Attributes:
        workbook_path:
            Absolute path to the workbook.

        worksheet_names:
            Names of all worksheets in workbook order.

        previous_material_count:
            Number of materials currently detected in the workbook.

        selected_sheet_names:
            Worksheets selected by the user for processing.
    """

    workbook_path: Path
    worksheet_names: List[str] = field(default_factory=list)
    previous_material_count: int = 0
    selected_sheet_names: List[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Normalize and validate workbook information."""

        self.workbook_path = Path(self.workbook_path).expanduser().resolve()

        if self.workbook_path.suffix.lower() not in {".xlsx", ".xlsm"}:
            raise ValueError(
                "Workbook must be an Excel file (.xlsx or .xlsm)."
            )

        if self.previous_material_count < 0:
            raise ValueError(
                "Previous material count cannot be negative."
            )

        normalized_sheet_names: List[str] = []
        for sheet_name in self.worksheet_names:
            sheet_name = str(sheet_name).strip()
            if sheet_name:
                normalized_sheet_names.append(sheet_name)

        self.worksheet_names = list(dict.fromkeys(normalized_sheet_names))

        normalized_selected: List[str] = []
        for sheet_name in self.selected_sheet_names:
            sheet_name = str(sheet_name).strip()
            if sheet_name:
                normalized_selected.append(sheet_name)

        self.selected_sheet_names = list(dict.fromkeys(normalized_selected))

    @property
    def workbook_name(self) -> str:
        """
        Returns the workbook file name.
        """
        return self.workbook_path.name

    @property
    def workbook_stem(self) -> str:
        """
        Returns the workbook name without its extension.
        """
        return self.workbook_path.stem

    @property
    def workbook_directory(self) -> Path:
        """
        Returns the directory containing the workbook.
        """
        return self.workbook_path.parent

    @property
    def worksheet_count(self) -> int:
        """
        Returns the number of worksheets in the workbook.
        """
        return len(self.worksheet_names)

    @property
    def selected_sheet_count(self) -> int:
        """
        Returns the number of selected worksheets.
        """
        return len(self.selected_sheet_names)

    def has_sheet(self, sheet_name: str) -> bool:
        """
        Returns whether the workbook contains the given worksheet.

        Args:
            sheet_name:
                Worksheet name.

        Returns:
            True if the worksheet exists; otherwise False.
        """
        return sheet_name.strip() in self.worksheet_names

    def is_sheet_selected(self, sheet_name: str) -> bool:
        """
        Returns whether the worksheet is selected for processing.

        Args:
            sheet_name:
                Worksheet name.

        Returns:
            True if selected; otherwise False.
        """
        return sheet_name.strip() in self.selected_sheet_names

    def select_sheet(self, sheet_name: str) -> None:
        """
        Marks a worksheet as selected.

        Duplicate selections are ignored.

        Args:
            sheet_name:
                Worksheet name.
        """
        sheet_name = sheet_name.strip()

        if (
            sheet_name
            and sheet_name in self.worksheet_names
            and sheet_name not in self.selected_sheet_names
        ):
            self.selected_sheet_names.append(sheet_name)

    def deselect_sheet(self, sheet_name: str) -> None:
        """
        Removes a worksheet from the selected list.

        Args:
            sheet_name:
                Worksheet name.
        """
        sheet_name = sheet_name.strip()

        if sheet_name in self.selected_sheet_names:
            self.selected_sheet_names.remove(sheet_name)

    def select_all(self) -> None:
        """
        Selects every worksheet.
        """
        self.selected_sheet_names = self.worksheet_names.copy()

    def clear_selection(self) -> None:
        """
        Clears all worksheet selections.
        """
        self.selected_sheet_names.clear()