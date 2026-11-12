n = int(input())
a = list(map(int, input().split()))
pos = []
neg = []
for i in range(n):
    if a[i] > 0:
        pos.append(a[i])
    elif a[i] < 0:
        neg.append(a[i])
print(f"{len(pos)} {len(neg)}")
if len(pos) == 0:
    print("-")
else:
    for x in pos:
        print(x,end = " ")
    print()
if len(neg) == 0:
    print("-")
else:
    for x in neg:
        print(x,end = " ")