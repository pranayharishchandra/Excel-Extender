"""
models/sheet_config.py

Data model representing a single worksheet configuration from the
'pranay_extension_config' worksheet.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class SheetConfig:
    """
    Configuration for a worksheet that participates in the
    formula extension process.

    Attributes:
        sheet_name:
            Name of the worksheet to process.

        template_start_row:
            The row containing the template formulas.
            Formula generation always starts from
            template_start_row + 1.

        rows_per_material:
            Number of worksheet rows occupied by one material block.

        managed_columns:
            List of Excel column letters that the application
            is allowed to clear and extend.

        preserve_existing:
            If True, existing formulas below the template are preserved.
            If False, managed formula cells are cleared before extension.
    """

    sheet_name: str
    template_start_row: int
    rows_per_material: int
    managed_columns: List[str] = field(default_factory=list)
    preserve_existing: bool = False

    def __post_init__(self) -> None:
        """
        Normalize and validate configuration values.
        """
        self.sheet_name = self.sheet_name.strip()

        if not self.sheet_name:
            raise ValueError("Sheet name cannot be empty.")

        if self.template_start_row < 1:
            raise ValueError("Template start row must be greater than zero.")

        if self.rows_per_material < 1:
            raise ValueError("Rows per material must be greater than zero.")

        normalized_columns: List[str] = []

        for column in self.managed_columns:
            if column is None:
                continue

            column = str(column).strip().upper()

            if not column:
                continue

            if not column.isalpha():
                raise ValueError(
                    f"Invalid managed column '{column}' "
                    f"for sheet '{self.sheet_name}'."
                )

            normalized_columns.append(column)

        if not normalized_columns:
            raise ValueError(
                f"Sheet '{self.sheet_name}' does not contain any managed columns."
            )

        # Remove duplicates while preserving order.
        self.managed_columns = list(dict.fromkeys(normalized_columns))

    @property
    def first_generated_row(self) -> int:
        """
        Returns the first row where formulas should be generated.
        """
        return self.template_start_row + 1

    def manages_column(self, column: str) -> bool:
        """
        Returns whether the specified Excel column is managed.

        Args:
            column:
                Excel column letter.

        Returns:
            True if the column is managed.
        """
        return column.strip().upper() in self.managed_columns