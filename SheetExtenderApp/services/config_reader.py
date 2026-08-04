"""
Reads worksheet configuration from the
'pranay_extension_config' worksheet.
"""

from __future__ import annotations

from typing import List

from openpyxl.workbook.workbook import Workbook

from models.sheet_config import SheetConfig
from common.column_utils import parse_managed_columns
from common.constants import (
    CONFIG_COLUMN_MANAGED_COLUMNS,
    CONFIG_COLUMN_PRESERVE_EXISTING,
    CONFIG_COLUMN_ROWS_PER_MATERIAL,
    CONFIG_COLUMN_SHEET_NAME,
    CONFIG_COLUMN_TEMPLATE_ROW,
    CONFIG_FIRST_DATA_ROW,
    CONFIG_SHEET_NAME,
)


def read_sheet_configs(workbook: Workbook) -> List[SheetConfig]:
    """
    Read all worksheet configurations from the configuration sheet.

    Parameters
    ----------
    workbook
        Loaded openpyxl workbook.

    Returns
    -------
    List[SheetConfig]
    """

    if CONFIG_SHEET_NAME not in workbook.sheetnames:
        raise ValueError(
            f"Configuration sheet '{CONFIG_SHEET_NAME}' not found."
        )

    config_sheet = workbook[CONFIG_SHEET_NAME]

    configs: List[SheetConfig] = []

    row = CONFIG_FIRST_DATA_ROW

    while True:

        sheet_name = config_sheet.cell(
            row=row,
            column=CONFIG_COLUMN_SHEET_NAME
        ).value

        # Empty sheet name means end of configuration.
        if sheet_name is None:
            break

        template_row = config_sheet.cell(
            row=row,
            column=CONFIG_COLUMN_TEMPLATE_ROW
        ).value

        rows_per_material = config_sheet.cell(
            row=row,
            column=CONFIG_COLUMN_ROWS_PER_MATERIAL
        ).value

        managed_columns = config_sheet.cell(
            row=row,
            column=CONFIG_COLUMN_MANAGED_COLUMNS
        ).value

        preserve_existing = config_sheet.cell(
            row=row,
            column=CONFIG_COLUMN_PRESERVE_EXISTING
        ).value

        configs.append(
            SheetConfig(
                sheet_name=str(sheet_name).strip(),
                template_start_row=int(template_row),
                rows_per_material=int(rows_per_material),
                managed_columns=parse_managed_columns(
                    str(managed_columns)
                ),
                preserve_existing=bool(preserve_existing),
            )
        )

        row += 1

    return configs