import os,sys, csv
from openpyxl import Workbook
wb = Workbook()
ws  = wb.active
ws.title  = "Sheet1"
def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    if not os.path.exists(csv_path):
        print("FileNotFoundError")
        sys.exit(1)
    if os.path.getsize(csv_path) == 0:
        print("ValueError")
        sys.exit(1)
    with open(csv_path ,"r", encoding="utf-8") as csv_file:
        for row in csv.reader(csv_file):
            ws.append(row)
        wb.save(xlsx_path)
csv_to_xlsx(r"C:\Users\eniko\PycharmProjects\PythonProject\data\samples\cities.csv", r"C:\Users\eniko\PycharmProjects\PythonProject\data\out\cities.xlsx")


