"""
commands/extend_command.py

Command responsible for extending formulas within a worksheet.
"""

from __future__ import annotations

from openpyxl.worksheet.worksheet import Worksheet

from commands.base_command import BaseCommand
from models.sheet_context import SheetContext
from services.formula_extender import FormulaExtender


class ExtendCommand(BaseCommand):
    """
    Command that extends formulas for the configured worksheet.
    """

    def __init__(
        self,
        formula_extender: FormulaExtender,
        *args,
        **kwargs,
    ) -> None:
        """
        Initialize the command.

        Args:
            formula_extender:
                Service responsible for extending formulas.
        """
        super().__init__(*args, **kwargs)
        self._formula_extender = formula_extender

    def execute(
        self,
        worksheet: Worksheet,
        context: SheetContext,
    ) -> None:
        """
        Execute the formula extension operation.

        Args:
            worksheet:
                Worksheet to process.

            context:
                Runtime processing context.
        """
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