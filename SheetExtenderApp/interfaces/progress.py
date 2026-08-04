"""
interfaces/progress.py

Interface for reporting progress during workbook processing.

Concrete implementations may update a GUI progress bar,
display console progress, or ignore progress updates entirely.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class IProgress(ABC):
    """
    Abstract progress reporting interface.
    """

    @abstractmethod
    def start(self, total_steps: int) -> None:
        """
        Initialize progress reporting.

        Args:
            total_steps:
                Total number of processing steps.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self, current_step: int, current_sheet: str) -> None:
        """
        Update the current progress.

        Args:
            current_step:
                Current completed step (1-based).

            current_sheet:
                Name of the worksheet currently being processed.
        """
        raise NotImplementedError

    @abstractmethod
    def finish(self) -> None:
        """
        Mark progress reporting as complete.
        """
        raise NotImplementedError