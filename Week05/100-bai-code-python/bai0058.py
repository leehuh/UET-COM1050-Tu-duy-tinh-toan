n = int(input())
a = [int(input()) for _ in range(n)]
dist_a = []
for x in a:
    if x not in dist_a:
        dist_a.append(x)
for x in dist_a:
    count = 0
    for y in a:
        if x == y:
            count += 1
    print(f"{x} {count}")