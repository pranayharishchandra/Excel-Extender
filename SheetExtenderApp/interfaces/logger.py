"""
interfaces/logger.py

Interface for application logging.

Concrete implementations may write log messages to the GUI,
console, file, or any other destination. The rest of the
application depends only on this interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class ILogger(ABC):
    """
    Abstract logger interface used throughout the application.
    """

    @abstractmethod
    def info(self, message: str) -> None:
        """
        Log an informational message.

        Args:
            message:
                Message to log.
        """
        raise NotImplementedError

    @abstractmethod
    def warning(self, message: str) -> None:
        """
        Log a warning message.

        Args:
            message:
                Message to log.
        """
        raise NotImplementedError

    @abstractmethod
    def error(self, message: str) -> None:
        """
        Log an error message.

        Args:
            message:
                Message to log.
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self) -> None:
        """
        Clear the current log output.
        """
        raise NotImplementedError