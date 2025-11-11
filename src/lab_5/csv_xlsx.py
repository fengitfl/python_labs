import os, csv, sys
from json_csv import check_csv_file

from openpyxl import Workbook
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not check_csv_file(csv_path):
        print("Error_CSV")
        sys.exit(1)

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            ws.append(row)


    for column_cells in ws.columns:
        max_length = 0
        column_letter = column_cells[0].column_letter
        for cell in column_cells:
            if cell.value:
                max_length = max(max_length, len(str(cell.value)))
        ws.column_dimensions[column_letter].width = max(max_length + 2, 8)
    wb.save(xlsx_path)
csv_to_xlsx(r"C:\Users\eniko\Gitrep\python_labs\data\samples\cities.csv", r"C:\Users\eniko\Gitrep\python_labs\data\out\cities.xlsx")


