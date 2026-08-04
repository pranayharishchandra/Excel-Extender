"""
gui/dialogs.py

Dialog helpers for the Excel Formula Extension Engine.

This module centralizes all user dialogs so the rest of the application
does not interact directly with tkinter's dialog APIs.
"""

from __future__ import annotations

from pathlib import Path
from tkinter import filedialog, messagebox

from common.constants import (
    DEFAULT_SAVE_AS_SUFFIX,
    SUPPORTED_WORKBOOK_EXTENSIONS,
    WORKBOOK_FILE_TYPES,
)


class Dialogs:
    """
    Helper class providing common file and message dialogs.
    """

    @staticmethod
    def select_workbook() -> Path | None:
        """
        Display a file picker for selecting an Excel workbook.

        Returns:
            Path to the selected workbook, or None if the dialog
            is cancelled.
        """
        filename = filedialog.askopenfilename(
            title="Select Excel Workbook",
            filetypes=WORKBOOK_FILE_TYPES,
        )

        if not filename:
            return None

        path = Path(filename)

        if path.suffix.lower() not in SUPPORTED_WORKBOOK_EXTENSIONS:
            messagebox.showerror(
                "Invalid File",
                "Please select a valid Excel workbook (.xlsx or .xlsm).",
            )
            return None

        return path

    @staticmethod
    def select_output_workbook(
        source_workbook: Path,
    ) -> Path | None:
        """
        Display a Save As dialog.

        The dialog defaults to the same folder as the selected workbook.

        Args:
            source_workbook:
                Original workbook selected by the user.

        Returns:
            Destination workbook path, or None if cancelled.
        """
        default_filename = (
            f"{source_workbook.stem}"
            f"{DEFAULT_SAVE_AS_SUFFIX}"
            f"{source_workbook.suffix}"
        )

        filename = filedialog.asksaveasfilename(
            title="Save Workbook As",
            initialdir=str(source_workbook.parent),
            initialfile=default_filename,
            defaultextension=source_workbook.suffix,
            filetypes=WORKBOOK_FILE_TYPES,
        )

        if not filename:
            return None

        return Path(filename)

    @staticmethod
    def confirm_save_original() -> bool:
        """
        Ask the user whether the original workbook should be overwritten.

        Returns:
            True if the user chooses to overwrite the workbook;
            otherwise False.
        """
        return messagebox.askyesno(
            "Save Original Workbook",
            (
                "This will overwrite the original workbook.\n\n"
                "Do you want to continue?"
            ),
            icon="warning",
        )

    @staticmethod
    def show_info(
        title: str,
        message: str,
    ) -> None:
        """
        Display an informational dialog.

        Args:
            title:
                Dialog title.

            message:
                Dialog message.
        """
        messagebox.showinfo(title, message)

    @staticmethod
    def show_warning(
        title: str,
        message: str,
    ) -> None:
        """
        Display a warning dialog.

        Args:
            title:
                Dialog title.

            message:
                Dialog message.
        """
        messagebox.showwarning(title, message)

    @staticmethod
    def show_error(
        title: str,
        message: str,
    ) -> None:
        """
        Display an error dialog.

        Args:
            title:
                Dialog title.

            message:
                Dialog message.
        """
        messagebox.showerror(title, message)