"""
models/processing_result.py

Represents the outcome of executing a processing command
(Clear, Extend, or Clear + Extend) on a workbook.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class ProcessingResult:
    """
    Stores the result of processing a workbook.

    Attributes:
        success:
            Indicates whether processing completed successfully.

        processed_sheets:
            Names of worksheets that were successfully processed.

        skipped_sheets:
            Names of worksheets that were skipped.

        messages:
            Informational messages generated during processing.

        error:
            Error message if processing failed; otherwise None.
    """

    success: bool = True
    processed_sheets: List[str] = field(default_factory=list)
    skipped_sheets: List[str] = field(default_factory=list)
    messages: List[str] = field(default_factory=list)
    error: str | None = None

    def add_processed_sheet(self, sheet_name: str) -> None:
        """
        Records a successfully processed worksheet.

        Args:
            sheet_name:
                Name of the worksheet.
        """
        sheet_name = sheet_name.strip()

        if sheet_name:
            self.processed_sheets.append(sheet_name)

    def add_skipped_sheet(self, sheet_name: str) -> None:
        """
        Records a skipped worksheet.

        Args:
            sheet_name:
                Name of the worksheet.
        """
        sheet_name = sheet_name.strip()

        if sheet_name:
            self.skipped_sheets.append(sheet_name)

    def add_message(self, message: str) -> None:
        """
        Adds an informational processing message.

        Args:
            message:
                Message to record.
        """
        message = message.strip()

        if message:
            self.messages.append(message)

    def set_error(self, message: str) -> None:
        """
        Marks the processing result as failed.

        Args:
            message:
                Error description.
        """
        message = message.strip()

        if not message:
            return

        self.success = False
        self.error = message

    @property
    def has_error(self) -> bool:
        """
        Returns True if processing failed.
        """
        return self.error is not None

    @property
    def processed_sheet_count(self) -> int:
        """
        Returns the number of processed worksheets.
        """
        return len(self.processed_sheets)

    @property
    def skipped_sheet_count(self) -> int:
        """
        Returns the number of skipped worksheets.
        """
        return len(self.skipped_sheets)

    @property
    def message_count(self) -> int:
        """
        Returns the number of informational messages.
        """
        return len(self.messages)