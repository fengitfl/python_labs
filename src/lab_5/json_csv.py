import csv, json, sys, os

import os
import json

def check_json_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл '{file_path}' не существует")
            return False
        
        if os.path.getsize(file_path) == 0:
            print(f"Ошибка: Файл '{file_path}' пустой")
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
        
        if not isinstance(json_data, list):
            print(f"Ошибка: JSON должен быть списком")
            return False
        
        if len(json_data) == 0:
            print("Ошибка: Список JSON пустой")
            return False
        
        if not all(isinstance(item, dict) for item in json_data):
            print("Ошибка: Не все элементы в списке являются словарями")
            return False
        print("Файл JSON прошел все проверки")
        return True
        
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        return False
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки файла: {e}")
        return False
    except PermissionError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return False

def check_csv_file(file_path: str) -> bool:
    try:
        if not os.path.exists(file_path):
            print(f"Ошибка: Файл '{file_path}' не существует")
            return False
        
        if os.path.getsize(file_path) == 0:
            print(f"Ошибка: Файл '{file_path}' пустой")
            return False
        
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            
            if header is None:
                print("Ошибка: CSV файл не содержит заголовка")
                return False
            
            if len(header) == 0:
                print("Ошибка: Заголовок CSV файла пустой")
                return False
            
            if any(not column.strip() for column in header):
                print("Ошибка: Заголовок CSV содержит пустые колонки")
                return False
        
        print("Файл CSV прошел все проверки")
        return True
        
    except csv.Error as e:
        print(f"Ошибка парсинга CSV: {e}")
        return False
    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки файла: {e}")
        return False
    except PermissionError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return False
    except StopIteration:
        print("Ошибка: Не удалось прочитать заголовок CSV файла")
        return False
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return False

def json_to_csv(json_path: str, csv_path: str) -> None:
    if not check_json_file(json_path):
        print("Error_JSON")
        sys.exit(1)

    with open(json_path, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)

    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    if not check_csv_file(csv_path):
        print("Error_CSV")
        sys.exit(1)

    with open(csv_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)
    
    with open(json_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False, indent=4)
csv_to_json(r"C:\Users\eniko\Gitrep\python_labs\data\samples\people.csv",r"C:\Users\eniko\Gitrep\python_labs\data\out\people_from_csv.json")


# json_to_csv(
#     r"C:\Users\eniko\PycharmProjects\PythonProject\data\samples\people.json",
#     r"C:\Users\eniko\PycharmProjects\PythonProject\data\out\people_from_json.csv"
# )
