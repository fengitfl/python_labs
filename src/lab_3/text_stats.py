import sys, os
# lib_dir = os.path.abspath(os.path.join(os.path.dirname(r'C:\Users\eniko\PycharmProjects\PythonProject\src\lib'), 'lib'))
# if lib_dir not in sys.path:
#     sys.path.append(lib_dir)
sys.path.append(r'C:\Users\eniko\PycharmProjects\PythonProject\src\lib')
from text import normalize, tokenize, count_freq, top_n
# def stats(words):
#     all_words = tokenize(words)
#     all_words= len(all_words)
#     unique_words = set(v.lower() for v in all_words)
#     result_list = len(list(unique_words))

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
    top5 = sorted(freqs.items(), key=lambda x: x[1], reverse=True)[:5]
    print("Топ-5:")
    print(table(top5, True))
if __name__ == "__main__":
    main(sys.stdin.buffer.read().decode("utf-8"))



