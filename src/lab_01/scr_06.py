N = int(input("N:"))
on_site_count = 0
distance_count = 0
k=1
for _ in range(N):
    data = input(f"in_{k}").split()
    participation_format = data[3] == 'True'
    if participation_format:
        on_site_count += 1
    else:
        distance_count += 1
    k+=1


print(on_site_count, distance_count)