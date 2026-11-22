n = int(input())
count = 0
for uoc in range(2, n + 1, 2):
    if n % uoc == 0:
        count += 1
print(count)

    