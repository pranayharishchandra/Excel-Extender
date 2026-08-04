"""
gui/logger.py

GUI implementation of the application logger.

Messages are written to a CustomTkinter textbox and timestamped.
"""

from __future__ import annotations

from datetime import datetime

import customtkinter as ctk

from common.constants import LOG_TIME_FORMAT
from interfaces.logger import ILogger


class GuiLogger(ILogger):
    """
    Logger implementation that writes messages to a CTkTextbox.
    """

    def __init__(
        self,
        textbox: ctk.CTkTextbox,
    ) -> None:
        """
        Initialize the GUI logger.

        Args:
            textbox:
                Textbox used as the application's log console.
        """
        self._textbox = textbox

        self._textbox.configure(state="disabled")

    def info(self, message: str) -> None:
        """
        Log an informational message.
        """
        self._append("INFO", message)

    def warning(self, message: str) -> None:
        """
        Log a warning message.
        """
        self._append("WARNING", message)

    def error(self, message: str) -> None:
        """
        Log an error message.
        """
        self._append("ERROR", message)

    def clear(self) -> None:
        """
        Clear the log console.
        """
        self._textbox.configure(state="normal")
        self._textbox.delete("1.0", "end")
        self._textbox.configure(state="disabled")
        self._textbox.update_idletasks()

    def _append(
        self,
        level: str,
        message: str,
    ) -> None:
        """
        Append a formatted log message.

        Args:
            level:
                Log level.

            message:
                Message text.
        """
        timestamp = datetime.now().strftime(LOG_TIME_FORMAT)

        line = f"[{timestamp}] [{level}] {message}\n"

        self._textbox.configure(state="normal")
        self._textbox.insert("end", line)
        self._textbox.see("end")
        self._textbox.configure(state="disabled")
        self._textbox.update_idletasks()