import sys
sys.path.append(r'C:\Users\eniko\PycharmProjects\PythonProject\src\lib')

from text import normalize, tokenize, count_freq, top_n

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
def main(text: str):
    text = text.strip()
    tokens = normalize(text)
    tokens = tokenize(tokens)
    freqs = count_freq(tokens)
    total_words = len(tokens)
    unique_words = len(freqs)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    top5 = sorted(freqs.items(), key=lambda x: (-x[1], x[0]))[:5]
    print("Топ-5:")
    print(table(top5, True))
