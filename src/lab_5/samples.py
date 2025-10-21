import json
from pathlib import Path

path = Path(r"C:\Users\eniko\Gitrep\python_labs\data\samples\people.json")
data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}]
with path.open("w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

with path.open(encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)
import csv

rows = [
     {"city": "seattle", "state": "WA", "population": "652405","land area": "83.9"},
     {"city": "new york", "state": "NY", "population": "8405837","land area": "302.6"},
     {"city": "boston", "state": "MA", "population": "645966","land area": "48.3"},
]
path = Path(r"C:\Users\eniko\Gitrep\python_labs\data\samples\cities.csv")
with path.open("w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)





