"""
Application-wide constants.

Avoid hardcoding strings and numbers throughout the project.
"""

from pathlib import Path

# ============================================================================
# Application
# ============================================================================

APP_NAME = "Excel Formula Extension Engine"
APP_VERSION = "1.0.0"

# ============================================================================
# Workbook Configuration
# ============================================================================

CONFIG_SHEET_NAME = "pranay_extension_config"
SOURCE_SHEET_NAME = "Sheet1"

# ============================================================================
# Template Defaults
# ============================================================================

DEFAULT_TEMPLATE_START_ROW = 2
FIRST_GENERATED_ROW = 3
HEADER_ROW = 1

# ============================================================================
# GUI
# ============================================================================

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 750

LOG_TIME_FORMAT = "%H:%M:%S"

# ============================================================================
# File Types
# ============================================================================

EXCEL_FILE_TYPES = [
    ("Excel Workbook", "*.xlsx"),
    ("Excel Macro Workbook", "*.xlsm"),
    ("All Files", "*.*"),
]

DEFAULT_OUTPUT_SUFFIX = "_Extended"

# ============================================================================
# Configuration Columns
# ============================================================================

CONFIG_COLUMN_SHEET_NAME = 1
CONFIG_COLUMN_TEMPLATE_ROW = 2
CONFIG_COLUMN_ROWS_PER_MATERIAL = 3
CONFIG_COLUMN_MANAGED_COLUMNS = 4
CONFIG_COLUMN_PRESERVE_EXISTING = 5

CONFIG_FIRST_DATA_ROW = 2

# ============================================================================
# Sheet1 Material Detection
# ============================================================================

# Column containing material numbers in Sheet1.
# Can be made configurable in the future if needed.
MATERIAL_COLUMN = 2  # Column B

# ============================================================================
# Logging
# ============================================================================

LOG_INFO = "INFO"
LOG_SUCCESS = "SUCCESS"
LOG_WARNING = "WARNING"
LOG_ERROR = "ERROR"

# ============================================================================
# Actions
# ============================================================================

ACTION_CLEAR = "CLEAR"
ACTION_EXTEND = "EXTEND"
ACTION_CLEAR_AND_EXTEND = "CLEAR_AND_EXTEND"

# ============================================================================
# Paths
# ============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"


# ============================================================================
# Configuration Sheet
# ============================================================================

CONFIG_SHEET_NAME = "pranay_extension_config"

HEADER_SHEET_NAME = "Sheet Name"
HEADER_TEMPLATE_ROW = "Template Start Row"
HEADER_ROWS_PER_MATERIAL = "Rows per Material"
HEADER_MANAGED_COLUMNS = "Managed Columns"
HEADER_PRESERVE_EXISTING = "Preserve Existing"

CONFIG_HEADER_ROW = 1
CONFIG_FIRST_DATA_ROW = 2