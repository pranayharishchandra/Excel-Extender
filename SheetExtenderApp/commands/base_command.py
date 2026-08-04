"""
commands/base_command.py

Abstract base class for worksheet processing commands.

Concrete commands implement one processing action:

- Clear
- Extend
- Clear + Extend

The Formula Engine executes commands through this common interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from openpyxl.worksheet.worksheet import Worksheet

from interfaces.logger import ILogger
from interfaces.progress import IProgress
from models.sheet_context import SheetContext


class BaseCommand(ABC):
    """
    Base class for all worksheet processing commands.
    """

    def __init__(
        self,
        logger: ILogger,
        progress: IProgress,
    ) -> None:
        """
        Initialize the command.

        Args:
            logger:
                Application logger implementation.

            progress:
                Progress reporting implementation.
        """
        self._logger = logger
        self._progress = progress

    @property
    def logger(self) -> ILogger:
        """
        Returns the configured logger.
        """
        return self._logger

    @property
    def progress(self) -> IProgress:
        """
        Returns the configured progress reporter.
        """
        return self._progress

    @abstractmethod
    def execute(
        self,
        worksheet: Worksheet,
        context: SheetContext,
    ) -> None:
        """
        Execute the command for a single worksheet.

        Args:
            worksheet:
                Worksheet to process.

            context:
                Runtime processing context.
        """
        raise NotImplementedError