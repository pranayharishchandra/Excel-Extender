"""
services/formula_extender.py

Service responsible for extending formulas in managed columns.

Formulas are generated using openpyxl's Translator so the behavior matches
Excel's drag-fill functionality.

Only managed columns are modified.

The template row is never changed.

Formulas are generated from:

    Template Row + 1
            ↓
    Target Last Row
"""

from __future__ import annotations

from openpyxl.formula.translate import Translator
from openpyxl.worksheet.worksheet import Worksheet

from models.sheet_context import SheetContext


class FormulaExtender:
    """
    Extends formulas for all managed columns in a worksheet.
    """

    def extend(
        self,
        worksheet: Worksheet,
        context: SheetContext,
    ) -> None:
        """
        Extend formulas for the configured worksheet.

        Args:
            worksheet:
                Worksheet being processed.

            context:
                Runtime processing context.
        """
        if not context.requires_extension:
            return

        template_row = context.template_row

        for column in context.managed_columns:
            self._extend_column(
                worksheet=worksheet,
                column=column,
                template_row=template_row,
                first_generated_row=context.first_generated_row,
                last_generated_row=context.target_last_row,
            )

    @staticmethod
    def _extend_column(
        worksheet: Worksheet,
        column: str,
        template_row: int,
        first_generated_row: int,
        last_generated_row: int,
    ) -> None:
        """
        Extend formulas for a single managed column.

        Args:
            worksheet:
                Worksheet being processed.

            column:
                Excel column letter.

            template_row:
                Row containing the template formula.

            first_generated_row:
                First row to generate.

            last_generated_row:
                Last row to generate.
        """
        template_cell = worksheet[f"{column}{template_row}"]
        template_value = template_cell.value

        # Nothing to extend if the template cell is empty or
        # does not contain a formula.
        if (
            template_value is None
            or not isinstance(template_value, str)
            or not template_value.startswith("=")
        ):
            return

        origin = template_cell.coordinate

        for target_row in range(
            first_generated_row,
            last_generated_row + 1,
        ):
            destination = f"{column}{target_row}"

            worksheet[destination].value = Translator(
                template_value,
                origin=origin,
            ).translate_formula(destination)