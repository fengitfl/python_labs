import os, csv, sys
from collections import Counter
from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab_3.text_stats import table
from io_txt_csv import read_text

input_files = [
    r"C:\Users\eniko\PycharmProjects\PythonProject\data\lab_4\a.txt",
    r"C:\Users\eniko\PycharmProjects\PythonProject\data\lab_4\b.txt",
]

for path in input_files:
    if not os.path.exists(path):
        print(f"Ошибка: входной файл '{path}' не найден.")
        sys.exit(1)


multiple_files = len(input_files) > 1

if multiple_files:
    print("Режим: несколько файлов\n")

    per_file_data = []
    total_freq = Counter()

    for path in input_files:
        text = read_text(path)
        words = tokenize(normalize(text))
        freq = Counter(words)
        total_freq.update(freq)

        for word, count in freq.items():
            per_file_data.append((os.path.basename(path), word, count))


    per_file_data.sort(key=lambda x: (x[0], -x[2], x[1]))

    output_dir = r"C:\Users\eniko\PycharmProjects\PythonProject\data"
    os.makedirs(output_dir, exist_ok=True)

    per_file_path = os.path.join(output_dir, "report_per_file.csv")
    with open(per_file_path, "w", encoding="cp65001", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["file", "word", "count"])
        writer.writerows(per_file_data)

    total_sorted = sorted(total_freq.items(), key=lambda x: (-x[1], x[0]))
    total_path = os.path.join(output_dir, "report_total.csv")
    with open(total_path, "w", encoding="cp65001", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(total_sorted)
in1 = True
if in1:
    print("Режим: один файл\n")

    path = r"C:\Users\eniko\PycharmProjects\PythonProject\data\lab_4\input.txt"
    text = read_text(path)
    words = tokenize(normalize(text))
    total_words = len(words)
    freqs = count_freq(words)
    unique_words = len(freqs)

    sorted_words = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))

    output_dir = r"C:\Users\eniko\PycharmProjects\PythonProject\data"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "report.csv")
    with open(output_path, "w", encoding="cp65001", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["word", "count"])
        writer.writerows(sorted_words)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}\n")
    print("Топ-5:")
    print(table(top_n(freqs, 5), True))

