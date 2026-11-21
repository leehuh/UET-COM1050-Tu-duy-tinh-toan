n = int(input())
while True:
    ds = list(map(int, input().split()))
    if len(ds) == n:
        break
for i in range(n - 1):
    for j in range(n - 1 - i):
        if ds[j] > ds[j + 1]:
            ds[j], ds[j + 1] = ds[j + 1], ds[j]
print(*ds)
