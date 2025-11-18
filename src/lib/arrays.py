p = []


def min_max(
    s,
):
    if s == p:
        return "ValueError"
    return min(s), max(s)


def unique_sorted(
    s,
):
    if s == p:
        return "ValueError"
    return list(set(sorted(s)))


def flatten(
    s,
):
    if s == p:
        return "ValueError"
    v = []
    for x in s:
        for i in x:
            if type(i) != int:
                return "TypeError"
            else:
                v.append((i))
    return v
