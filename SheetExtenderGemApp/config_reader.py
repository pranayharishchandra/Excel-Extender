"""Handles the reading and validation of the internal Excel configuration sheet."""

from typing import List
from openpyxl.worksheet.worksheet import Worksheet
from models import SheetConfig
from column_utils import parse_managed_columns

def read_configuration(config_sheet: Worksheet) -> List[SheetConfig]:
    """
    Reads the permanent worksheet metadata from the config sheet.
    Validates structural integrity before continuing.
    """
    configs = []
    seen_sheets = set()
    
    # Row 1 is header. Read data continuously starting from Row 2.
    for row_idx, row in enumerate(config_sheet.iter_rows(min_row=2, values_only=True), start=2):
        if not row[0]:
            continue
            
        sheet_name = str(row[0]).strip()
        
        # Validation checks
        if sheet_name in seen_sheets:
            raise ValueError(f"Duplicate configuration found for sheet: {sheet_name}")
        seen_sheets.add(sheet_name)
        
        try:
            template_row = int(row[1])
            rows_per_mat = int(row[2])
            managed_cols_str = str(row[3]) if row[3] else ""
            preserve_str = str(row[4]).strip().lower() if row[4] else "no"
            
            if rows_per_mat <= 0:
                raise ValueError(f"Rows per material must be > 0. Found {rows_per_mat} in {sheet_name}.")
            if template_row <= 0:
                raise ValueError(f"Template row must be > 0. Found {template_row} in {sheet_name}.")
                
            preserve_existing = preserve_str in ('yes', 'y', 'true', '1')
            managed_cols = parse_managed_columns(managed_cols_str)
            
            configs.append(SheetConfig(
                sheet_name=sheet_name,
                template_start_row=template_row,
                rows_per_material=rows_per_mat,
                managed_columns=managed_cols,
                preserve_existing=preserve_existing
            ))
            
        except (ValueError, TypeError) as e:
            raise ValueError(f"Error parsing configuration at row {row_idx}: {str(e)}")
            
    return configs