import os, csv, sys
from collections import Counter
from src.lab_3.text import normalize, tokenize, top_n, count_freq
from src.lib.io_txt_csv import read_text
def table(arr: list[tuple[str, int]], isTable: bool = True) -> str:
    if not arr:
        return "(нет данных)"
    s = str()
    if isTable:
        word_col_width = max(len("слово"), max(len(a[0]) for a in arr))
        freq_col_width = max(len("частота"), max(len(str(a[1])) for a in arr))
        s += f"{'слово'.ljust(word_col_width)} | {'частота'.rjust(freq_col_width)}"
        s += "\n" + "-" * word_col_width + "-+-" + "-" * freq_col_width
        for word, freq in arr:
            s += f"\n{word.ljust(word_col_width)} | {str(freq).rjust(freq_col_width)}"
        return s
    else:
        return "\n".join(f"{a[0]}: {a[1]}" for a in arr)

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
    print("Режим несколько файлов: выполнен\n")

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
    print("Режим один файл:")

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
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    print(table(top_n(freqs, 5), True))

