import csv, os,sys
from pathlib import Path

def read_text(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать '{path}'. Попробуйте encoding='cp65001'")
        sys.exit(1)
    except FileNotFoundError:
        print("Файл не найден, укажите полный путь к файлу")
        return ""


def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
        with open(path, 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            if header:
                writer.writerow(header)
            lenr = len(rows[0])
            for row in rows:
                if len(row) != lenr:
                    print("ValueError")
            writer.writerows(rows)


def create_directory(directory_path):
    try:
        os.makedirs(directory_path, exist_ok=True)
        print(f"Директория создана или уже существует: {directory_path}")
        return True
    except Exception as e:
        print(f"Ошибка при создании директории: {e}")
        return False
# txt = read_text(r"C:\Users\eniko\PycharmProjects\PythonProject\data\lab_4\input.txt")
# print(txt)
# print(write_csv([("word","count"),("test",3)], r"C:\Users\eniko\PycharmProjects\PythonProject\data\check.csv"))

