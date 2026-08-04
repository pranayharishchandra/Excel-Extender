# Excel Formula Extension Engine

A production-quality desktop application for extending SAP Excel material creation templates using Excel-style formula translation.

The application is built with:

- Python 3.11+
- CustomTkinter
- openpyxl

---

# Features

- Automatically detects existing material count
- Reads worksheet configuration from a dedicated configuration sheet
- Dynamic header detection (no hardcoded column positions)
- Extend formulas exactly like Excel drag-fill
- Clear generated formulas
- Clear + Extend in one operation
- Supports multiple worksheets
- Select individual worksheets
- Save Original or Save As
- Progress bar
- Live logging console

---

# Project Structure

```text
excel_formula_extension/
│
├── main.py
├── requirements.txt
├── README.md
│
├── assets/
│
├── gui/
│   ├── app.py
│   ├── dialogs.py
│   ├── logger.py
│   └── widgets.py
│
├── commands/
│   ├── base_command.py
│   ├── clear_command.py
│   ├── extend_command.py
│   └── clear_extend_command.py
│
├── core/
│   └── formula_engine.py
│
├── services/
│   ├── config_reader.py
│   ├── formula_clearer.py
│   ├── formula_extender.py
│   ├── material_detector.py
│   └── validator.py
│
├── common/
│   ├── constants.py
│   ├── column_utils.py
│   └── excel_headers.py
│
├── interfaces/
│   ├── logger.py
│   └── progress.py
│
└── models/
    ├── sheet_config.py
    ├── sheet_context.py
    ├── validation_result.py
    ├── processing_result.py
    └── workbook_info.py
```

---

# Configuration Worksheet

The workbook **must** contain a worksheet named:

```text
pranay_extension_config
```

The configuration worksheet is identified by header names rather than fixed column positions.

Required headers:

| Header | Description |
|---------|-------------|
| Sheet Name | Worksheet to process |
| Template Start Row | Row containing the template formulas |
| Rows per Material | Number of rows occupied by one material |
| Managed Columns | Comma-separated Excel columns that may be modified |
| Preserve Existing | TRUE/FALSE |

Example:

| Sheet Name | Template Start Row | Rows per Material | Managed Columns | Preserve Existing |
|------------|-------------------|-------------------|-----------------|-------------------|
| Sheet2 | 2 | 36 | B,C,D,E,F,G,H | FALSE |
| Sheet3 | 5 | 28 | B,C,E,H,J | TRUE |

---

# Formula Rules

The application always uses:

```python
openpyxl.formula.translate.Translator
```

No regular expressions are used.

No manual formula manipulation is performed.

Generated formulas behave exactly like dragging formulas in Microsoft Excel.

---

# Clear Operation

Only managed columns are cleared.

Rows cleared:

```text
Template Row + 1
↓
Previous Last Row
```

The template row is never modified.

---

# Extend Operation

Formulas are generated using the template row.

Rows generated:

```text
Template Row + 1
↓
Target Last Row
```

---

# GUI

The application provides:

- Workbook selector
- Previous material count
- New material count
- Sheet selector
- Select All
- Select None
- Save Original
- Save As
- Clear
- Extend
- Clear + Extend
- Progress bar
- Current worksheet indicator
- Scrolling log console

---

# Installation

Clone the repository.

Create a virtual environment.

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running

```bash
python main.py
```

---

# Workflow

```text
Select Workbook
        │
        ▼
Read Configuration
        │
        ▼
Validate Workbook
        │
        ▼
Detect Existing Materials
        │
        ▼
Choose Output
        │
        ▼
Select Worksheets
        │
        ▼
Choose Action

    Clear
    Extend
    Clear + Extend

        │
        ▼
Save Workbook
```

---

# Notes

- Workbook structure is never modified.
- Worksheets are never added or deleted.
- Worksheet names are never changed.
- Only configured managed columns are modified.
- The template row is always preserved.
- The application is designed specifically for SAP material creation templates.

---

# License

This project is intended for internal automation and productivity workflows.