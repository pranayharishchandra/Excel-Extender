"""
commands/clear_command.py

Command responsible for clearing generated formulas from a worksheet.
"""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet

from commands.base_command import BaseCommand
from models.sheet_context import SheetContext
from services.formula_clearer import FormulaClearer


class ClearCommand(BaseCommand):
    """
    Command that clears generated formulas from the configured worksheet.
    """

    def __init__(
        self,
        formula_clearer: FormulaClearer,
        *args,
        **kwargs,
    ) -> None:
        """
        Initialize the command.

        Args:
            formula_clearer:
                Service responsible for clearing formulas.
        """
        super().__init__(*args, **kwargs)
        self._formula_clearer = formula_clearer

    def execute(
        self,
        worksheet: Worksheet,
        context: SheetContext,
    ) -> None:
        """
        Execute the clear operation.

        Args:
            worksheet:
                Worksheet to process.

            context:
                Runtime processing context.
        """
        self.logger.info(
            f"Clearing formulas in worksheet '{context.sheet_name}'."
        )

        self._formula_clearer.clear(
            worksheet=worksheet,
            context=context,
        )

        self.logger.info(
            f"Finished clearing worksheet '{context.sheet_name}'."
        )