"""
gui/widgets.py

Reusable CustomTkinter widgets for the Excel Formula Extension Engine.
"""

from __future__ import annotations

import customtkinter as ctk


class LabeledEntry(ctk.CTkFrame):
    """
    Frame containing a label and an entry widget.
    """

    def __init__(
        self,
        master,
        label: str,
        width: int = 180,
        **kwargs,
    ) -> None:
        super().__init__(master, fg_color="transparent", **kwargs)

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.label = ctk.CTkLabel(
            self,
            text=label,
            anchor="w",
        )
        self.label.grid(
            row=0,
            column=0,
            padx=(0, 10),
            pady=2,
            sticky="w",
        )

        self.entry = ctk.CTkEntry(
            self,
            width=width,
        )
        self.entry.grid(
            row=0,
            column=1,
            sticky="ew",
        )

    def get(self) -> str:
        """
        Returns the entry value.
        """
        return self.entry.get().strip()

    def set(self, value: str) -> None:
        """
        Sets the entry value.
        """
        self.entry.delete(0, "end")
        self.entry.insert(0, str(value))

    def clear(self) -> None:
        """
        Clears the entry.
        """
        self.entry.delete(0, "end")

    def configure_state(self, state: str) -> None:
        """
        Enables or disables the entry.
        """
        self.entry.configure(state=state)


class LabeledComboBox(ctk.CTkFrame):
    """
    Frame containing a label and a combo box.
    """

    def __init__(
        self,
        master,
        label: str,
        values: list[str] | None = None,
        width: int = 180,
        **kwargs,
    ) -> None:
        super().__init__(master, fg_color="transparent", **kwargs)

        if values is None:
            values = []

        self.grid_columnconfigure(1, weight=1)

        self.label = ctk.CTkLabel(
            self,
            text=label,
            anchor="w",
        )
        self.label.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="w",
        )

        self.combobox = ctk.CTkComboBox(
            self,
            values=values,
            width=width,
        )
        self.combobox.grid(
            row=0,
            column=1,
            sticky="ew",
        )

    def get(self) -> str:
        """
        Returns the selected value.
        """
        return self.combobox.get()

    def set(self, value: str) -> None:
        """
        Sets the selected value.
        """
        self.combobox.set(value)

    def set_values(
        self,
        values: list[str],
    ) -> None:
        """
        Replaces the combo box values.
        """
        self.combobox.configure(values=values)

        if values:
            self.combobox.set(values[0])

    def configure_state(
        self,
        state: str,
    ) -> None:
        """
        Enables or disables the combo box.
        """
        self.combobox.configure(state=state)


class SheetList(ctk.CTkScrollableFrame):
    """
    Scrollable list of worksheet checkboxes.
    """

    def __init__(
        self,
        master,
        **kwargs,
    ) -> None:
        super().__init__(master, **kwargs)

        self._checkboxes: dict[str, ctk.CTkCheckBox] = {}

    def set_sheets(
        self,
        sheet_names: list[str],
    ) -> None:
        """
        Populate the sheet list.
        """
        self.clear()

        for row, sheet_name in enumerate(sheet_names):
            checkbox = ctk.CTkCheckBox(
                self,
                text=sheet_name,
            )

            checkbox.select()

            checkbox.grid(
                row=row,
                column=0,
                padx=5,
                pady=4,
                sticky="w",
            )

            self._checkboxes[sheet_name] = checkbox

    def get_selected(self) -> list[str]:
        """
        Returns all selected worksheet names.
        """
        return [
            name
            for name, checkbox in self._checkboxes.items()
            if checkbox.get() == 1
        ]

    def select_all(self) -> None:
        """
        Select every worksheet.
        """
        for checkbox in self._checkboxes.values():
            checkbox.select()

    def deselect_all(self) -> None:
        """
        Deselect every worksheet.
        """
        for checkbox in self._checkboxes.values():
            checkbox.deselect()

    def clear(self) -> None:
        """
        Remove every checkbox.
        """
        for checkbox in self._checkboxes.values():
            checkbox.destroy()

        self._checkboxes.clear()


class ProgressPanel(ctk.CTkFrame):
    """
    Progress bar and current worksheet display.
    """

    def __init__(
        self,
        master,
        **kwargs,
    ) -> None:
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        self.sheet_label = ctk.CTkLabel(
            self,
            text="Current Sheet: -",
            anchor="w",
        )
        self.sheet_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5),
            sticky="ew",
        )

        self.progress_bar = ctk.CTkProgressBar(self)
        self.progress_bar.grid(
            row=1,
            column=0,
            padx=10,
            pady=(0, 10),
            sticky="ew",
        )

        self.progress_bar.set(0.0)

    def update_progress(
        self,
        current: int,
        total: int,
        sheet_name: str,
    ) -> None:
        """
        Update the displayed progress.
        """
        self.sheet_label.configure(
            text=f"Current Sheet: {sheet_name}"
        )

        progress = 0.0 if total <= 0 else current / total

        self.progress_bar.set(progress)
        self.update_idletasks()

    def reset(self) -> None:
        """
        Reset the progress display.
        """
        self.sheet_label.configure(
            text="Current Sheet: -"
        )
        self.progress_bar.set(0.0)