"""
main.py

Application entry point for the Excel Formula Extension Engine.
"""

from __future__ import annotations

import customtkinter as ctk

from gui.app import App


def main() -> None:
    """
    Configure CustomTkinter and start the application.
    """
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    app = App()
    app.run()


if __name__ == "__main__":
    main()