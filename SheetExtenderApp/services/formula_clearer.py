"""
services/formula_clearer.py

Service responsible for clearing generated formulas from managed columns.

Only managed columns are cleared.

The template row is never modified.

Only rows between

    Template Row + 1
            ↓
    Previous Last Row

are cleared.
"""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet

from models.sheet_context import SheetContext


class FormulaClearer:
    """
    Clears generated formulas from a worksheet.

    This service never deletes rows, inserts rows or modifies worksheet
    structure. It only clears cell values in managed columns.
    """

    def clear(
        self,
        worksheet: Worksheet,
        context: SheetContext,
    ) -> None:
        """
        Clear generated formulas from the worksheet.

        Args:
            worksheet:
                Worksheet to clear.

            context:
                Runtime processing context.

        Returns:
            None
        """
        if not context.requires_clearing:
            return

        first_row = context.first_generated_row
        last_row = context.previous_last_row

        for column in context.managed_columns:
            self._clear_column(
                worksheet=worksheet,
                column=column,
                first_row=first_row,
                last_row=last_row,
            )

    @staticmethod
    def _clear_column(
        worksheet: Worksheet,
        column: str,
        first_row: int,
        last_row: int,
    ) -> None:
        """
        Clear a single managed column.

        Args:
            worksheet:
                Worksheet being processed.

            column:
                Excel column letter.

            first_row:
                First row to clear.

            last_row:
                Last row to clear.
        """
        for row in range(first_row, last_row + 1):
            worksheet[f"{column}{row}"].value = None