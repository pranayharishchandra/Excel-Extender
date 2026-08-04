from openpyxl import load_workbook

wb = load_workbook(
    r"C:\Users\PranayHarishchandra\Desktop\Excel Extender\test\Pranay Master ZMP1.xlsx"
)

wb.save(
    r"C:\Users\PranayHarishchandra\Desktop\Excel Extender\test.xlsx"
)

wb.close()

print("Done")