"""Utility functions for workbook analysis and row calculations."""

from openpyxl.worksheet.worksheet import Worksheet

def detect_material_count(sheet: Worksheet) -> int:
    """
    Detects the number of materials in the designated source sheet (e.g., Sheet1).
    Assumes row 1 is the header. Scans column A for the last populated cell 
    to prevent artificially inflated max_row values from rogue formatting.
    """
    last_non_empty = 1
    
    # iter_rows handles large amounts of formatting safely
    for row_idx, row in enumerate(sheet.iter_rows(min_col=1, max_col=1, values_only=True), start=1):
        val = row[0]
        if val is not None and str(val).strip() != "":
            last_non_empty = row_idx
            
    # Subtract 1 because Row 1 is the header
    return last_non_empty - 1 if last_non_empty > 1 else 0


def calculate_last_row(template_start_row: int, num_materials: int, rows_per_material: int) -> int:
    """
    Calculates the exact last row targeted based on the material count.
    """
    if num_materials <= 0:
        return template_start_row
    return template_start_row + (num_materials * rows_per_material) - 1