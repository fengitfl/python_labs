N = int(input())
count_true = 0
count_false = 0

for _ in range(N):
    surname, name, age, format_part = input().split()
    if format_part == "True":
        count_true += 1
    else:
        count_false += 1

print(count_true, count_false)
