ds = [int(input()) for _ in range(4)]
max = ds[0]
for i in range(len(ds)):
    if max < ds[i]:
        max = ds[i]
print(max)