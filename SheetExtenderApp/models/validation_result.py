"""
models/validation_result.py

Validation result model used throughout the application to communicate
whether a workbook or processing step is valid, along with any errors
or warnings encountered.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(slots=True)
class ValidationResult:
    """
    Represents the outcome of a validation operation.

    Attributes:
        is_valid:
            Indicates whether validation succeeded.

        errors:
            Fatal validation errors that prevent processing.

        warnings:
            Non-fatal validation warnings that should be shown to the user.
    """

    is_valid: bool = True
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def add_error(self, message: str) -> None:
        """
        Adds a validation error and marks the result as invalid.

        Args:
            message:
                Error description.
        """
        message = message.strip()

        if not message:
            return

        self.errors.append(message)
        self.is_valid = False

    def add_warning(self, message: str) -> None:
        """
        Adds a non-fatal validation warning.

        Args:
            message:
                Warning description.
        """
        message = message.strip()

        if not message:
            return

        self.warnings.append(message)

    @property
    def has_errors(self) -> bool:
        """
        Returns True if one or more validation errors exist.
        """
        return bool(self.errors)

    @property
    def has_warnings(self) -> bool:
        """
        Returns True if one or more validation warnings exist.
        """
        return bool(self.warnings)

    @property
    def error_count(self) -> int:
        """
        Returns the number of validation errors.
        """
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        """
        Returns the number of validation warnings.
        """
        return len(self.warnings)

    def merge(self, other: "ValidationResult") -> None:
        """
        Merges another ValidationResult into this instance.

        Args:
            other:
                Validation result to merge.
        """
        if not isinstance(other, ValidationResult):
            raise TypeError(
                "other must be an instance of ValidationResult."
            )

        if other.errors:
            self.errors.extend(other.errors)

        if other.warnings:
            self.warnings.extend(other.warnings)

        self.is_valid = not self.errors

    @classmethod
    def success(cls) -> "ValidationResult":
        """
        Creates a successful validation result.
        """
        return cls(is_valid=True)

    @classmethod
    def failure(cls, message: str) -> "ValidationResult":
        """
        Creates a failed validation result with a single error.

        Args:
            message:
                Error description.
        """
        result = cls(is_valid=False)
        result.add_error(message)
        return result
