def selection_sort(ds):
    for i in range(len(ds)):
        min_index = i
        for j in range(i, len(ds)):
            if ds[j] < ds[min_index]:
                min_index = j
        ds[i], ds[min_index] = ds[min_index], ds[i]
    return ds
a = list(map(int, input().split()))
selection_sort(a)
max2 = None
for i in range(len(a) - 1, -1, -1):
    if a[i] < a[len(a)-1]:
        max2 = a[i]
        break
if max2 == None:
    print("-")
else:
    print(max2)