def decode(s):
    for i, ch in enumerate(s):
        if ch.isupper():
            start_index = i
            break
    result = [s[start_index]]

    for i, ch in enumerate(s):
        if ch.isdigit():
            second_index = i + 1
            result.append(s[second_index])
            break

    step = second_index - start_index
    i = second_index + step
    while i < len(s):
        result.append(s[i])
        if s[i] == '.':
            break
        i += step

    return ''.join(result)

s=input("in:")
print(decode(s))

