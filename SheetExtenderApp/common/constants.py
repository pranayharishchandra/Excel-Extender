"""
common/constants.py

Application-wide constants used throughout the Excel Formula
Extension Engine.
"""

from __future__ import annotations

from pathlib import Path

# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

APPLICATION_NAME: str = "Excel Formula Extension Engine"
APPLICATION_VERSION: str = "1.0.0"

# ---------------------------------------------------------------------------
# Workbook Configuration
# ---------------------------------------------------------------------------

CONFIG_SHEET_NAME: str = "pranay_extension_config"

# ---------------------------------------------------------------------------
# Configuration Headers
# ---------------------------------------------------------------------------

HEADER_SHEET_NAME: str = "Sheet Name"
HEADER_TEMPLATE_START_ROW: str = "Template Start Row"
HEADER_ROWS_PER_MATERIAL: str = "Rows per Material"
HEADER_MANAGED_COLUMNS: str = "Managed Columns"
HEADER_PRESERVE_EXISTING: str = "Preserve Existing"

CONFIG_REQUIRED_HEADERS: tuple[str, ...] = (
    HEADER_SHEET_NAME,
    HEADER_TEMPLATE_START_ROW,
    HEADER_ROWS_PER_MATERIAL,
    HEADER_MANAGED_COLUMNS,
    HEADER_PRESERVE_EXISTING,
)

# ---------------------------------------------------------------------------
# Worksheet Processing
# ---------------------------------------------------------------------------

FIRST_WORKSHEET_ROW: int = 1
FIRST_EXCEL_COLUMN: int = 1

# ---------------------------------------------------------------------------
# Supported Workbook Formats
# ---------------------------------------------------------------------------

SUPPORTED_WORKBOOK_EXTENSIONS: frozenset[str] = frozenset(
    {
        ".xlsx",
        ".xlsm",
    }
)

# ---------------------------------------------------------------------------
# File Dialog Filters
# ---------------------------------------------------------------------------

WORKBOOK_FILE_TYPES: tuple[tuple[str, str], ...] = (
    ("Excel Workbook", "*.xlsx"),
    ("Excel Macro-Enabled Workbook", "*.xlsm"),
    ("All Excel Files", "*.xlsx *.xlsm"),
)

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

DEFAULT_SAVE_AS_SUFFIX: str = "_extended"

# ---------------------------------------------------------------------------
# GUI Defaults
# ---------------------------------------------------------------------------

DEFAULT_WINDOW_WIDTH: int = 1100
DEFAULT_WINDOW_HEIGHT: int = 760
MIN_WINDOW_WIDTH: int = 900
MIN_WINDOW_HEIGHT: int = 650

PROGRESS_MINIMUM: int = 0
PROGRESS_MAXIMUM: int = 100

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

LOG_TIME_FORMAT: str = "%H:%M:%S"

# ---------------------------------------------------------------------------
# Boolean Values Accepted in Configuration
# ---------------------------------------------------------------------------

TRUE_VALUES: frozenset[str] = frozenset(
    {
        "1",
        "TRUE",
        "YES",
        "Y",
    }
)

FALSE_VALUES: frozenset[str] = frozenset(
    {
        "0",
        "FALSE",
        "NO",
        "N",
        "",
    }
)

# ---------------------------------------------------------------------------
# Managed Columns
# ---------------------------------------------------------------------------

MANAGED_COLUMN_SEPARATOR: str = ","

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
ASSETS_DIRECTORY: Path = PROJECT_ROOT / "assets"