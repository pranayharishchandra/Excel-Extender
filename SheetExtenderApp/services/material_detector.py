"""
services/material_detector.py

Service responsible for detecting the number of existing material blocks
within a worksheet.

Detection is based solely on the configured worksheet structure:

- Template Start Row
- Rows per Material

The detector does not inspect formulas or workbook configuration beyond
what is required to determine the last populated material block.
"""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet

from models.sheet_config import SheetConfig


class MaterialDetector:
    """
    Detects the number of existing material blocks in a worksheet.
    """

    def detect_material_count(
        self,
        worksheet: Worksheet,
        config: SheetConfig,
    ) -> int:
        """
        Detect the number of materials currently present.

        Args:
            worksheet:
                Worksheet to inspect.

            config:
                Configuration for the worksheet.

        Returns:
            Number of detected material blocks.
        """
        last_row = self.detect_last_material_row(worksheet, config)

        if last_row <= config.template_start_row:
            return 1

        generated_rows = last_row - config.template_start_row

        additional_materials = (
            generated_rows // config.rows_per_material
        )

        return 1 + additional_materials

    def detect_last_material_row(
        self,
        worksheet: Worksheet,
        config: SheetConfig,
    ) -> int:
        """
        Detect the last row belonging to the material data.

        Empty rows at the bottom of the worksheet are ignored.

        Args:
            worksheet:
                Worksheet to inspect.

            config:
                Sheet configuration.

        Returns:
            Last populated row belonging to the material section.
            Returns the template row if no generated rows exist.
        """
        last_used_row = self._find_last_used_row(worksheet)

        if last_used_row <= config.template_start_row:
            return config.template_start_row

        generated_rows = last_used_row - config.template_start_row

        completed_blocks = (
            generated_rows // config.rows_per_material
        )

        return (
            config.template_start_row
            + completed_blocks * config.rows_per_material
        )

    @staticmethod
    def _find_last_used_row(
        worksheet: Worksheet,
    ) -> int:
        """
        Find the last non-empty row in the worksheet.

        A row is considered used if at least one cell contains
        a value or a formula.

        Args:
            worksheet:
                Worksheet to inspect.

        Returns:
            1-based last used row.
        """
        for row in range(worksheet.max_row, 0, -1):
            for cell in worksheet[row]:
                if cell.value is not None:
                    if str(cell.value).strip():
                        return row
        return 1