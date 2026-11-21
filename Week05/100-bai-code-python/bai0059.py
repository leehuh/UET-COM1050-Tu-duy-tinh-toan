n = int(input())
a = [int(input()) for _ in range(n)]
dist_a = []
count_a = []
for x in a:
    if x not in dist_a:
        dist_a.append(x)
for x in dist_a:
    count = 0
    for y in a:
        if x == y:
            count += 1
    count_a.append(count)
max_index = 0
for i in range(len(count_a)):
    if count_a[i] > count_a[max_index]:
        max_index = i
print(dist_a[max_index], count_a[max_index])
        
    