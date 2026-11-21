n = int(input())
ds = list(map(int, input().split()))
max = ds[0]
index = 0
for i in range(n):
    if ds[i] > max:
        max = ds[i]
        index = i
print(max, index)