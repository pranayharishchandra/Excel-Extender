"""
models/sheet_context.py

Runtime context for processing a single worksheet.
"""

from __future__ import annotations

from dataclasses import dataclass

from .sheet_config import SheetConfig


@dataclass(slots=True)
class SheetContext:
    """
    Holds the runtime state for processing a single worksheet.

    This object is created after configuration has been read and
    material counts have been determined. It provides all information
    required by the validator, commands, and formula services.

    Attributes:
        config:
            Configuration for the worksheet.

        previous_material_count:
            Number of material blocks currently present in the worksheet.

        target_material_count:
            Number of material blocks requested by the user.

        previous_last_row:
            Last row belonging to the existing material data.

        target_last_row:
            Last row required after extending formulas.

        selected:
            Indicates whether this worksheet has been selected for
            processing by the user.
    """

    config: SheetConfig
    previous_material_count: int
    target_material_count: int
    previous_last_row: int
    target_last_row: int
    selected: bool = True

    def __post_init__(self) -> None:
        """Validate runtime values."""

        if self.previous_material_count < 0:
            raise ValueError("Previous material count cannot be negative.")

        if self.target_material_count < 0:
            raise ValueError("Target material count cannot be negative.")

        if self.previous_last_row < self.config.template_start_row:
            raise ValueError(
                "Previous last row cannot be above the template row."
            )

        if self.target_last_row < self.config.template_start_row:
            raise ValueError(
                "Target last row cannot be above the template row."
            )

    @property
    def template_row(self) -> int:
        """Returns the template row."""
        return self.config.template_start_row

    @property
    def first_generated_row(self) -> int:
        """Returns the first row where formulas may be generated."""
        return self.config.first_generated_row

    @property
    def rows_per_material(self) -> int:
        """Returns the configured rows per material."""
        return self.config.rows_per_material

    @property
    def sheet_name(self) -> str:
        """Returns the worksheet name."""
        return self.config.sheet_name

    @property
    def managed_columns(self) -> list[str]:
        """Returns the managed Excel columns."""
        return self.config.managed_columns

    @property
    def preserve_existing(self) -> bool:
        """Returns whether existing formulas should be preserved."""
        return self.config.preserve_existing

    @property
    def material_delta(self) -> int:
        """
        Returns the difference between the target and current
        material counts.
        """
        return self.target_material_count - self.previous_material_count

    @property
    def requires_extension(self) -> bool:
        """Returns True if additional material rows must be generated."""
        return self.target_last_row > self.previous_last_row

    @property
    def requires_clearing(self) -> bool:
        """
        Returns True if there are existing generated rows below the
        template row that can be cleared.
        """
        return self.previous_last_row >= self.first_generated_row