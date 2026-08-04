"""
commands/clear_extend_command.py

Command responsible for clearing existing generated formulas and then
extending formulas for a worksheet.

Execution order:

    1. Clear
    2. Extend
"""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet

from commands.base_command import BaseCommand
from models.sheet_context import SheetContext
from services.formula_clearer import FormulaClearer
from services.formula_extender import FormulaExtender


class ClearExtendCommand(BaseCommand):
    """
    Command that first clears generated formulas and then extends them
    using the configured template row.
    """

    def __init__(
        self,
        formula_clearer: FormulaClearer,
        formula_extender: FormulaExtender,
        *args,
        **kwargs,
    ) -> None:
        """
        Initialize the command.

        Args:
            formula_clearer:
                Service responsible for clearing formulas.

            formula_extender:
                Service responsible for extending formulas.
        """
        super().__init__(*args, **kwargs)

        self._formula_clearer = formula_clearer
        self._formula_extender = formula_extender

    def execute(
        self,
        worksheet: Worksheet,
        context: SheetContext,
    ) -> None:
        """
        Execute the Clear + Extend workflow.

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

        self.logger.info(
            f"Extending formulas in worksheet '{context.sheet_name}'."
        )

        self._formula_extender.extend(
            worksheet=worksheet,
            context=context,
        )

        self.logger.info(
            f"Finished extending worksheet '{context.sheet_name}'."
        )