a = []
while True:
    try:
        x = int(input())
        a.append(x)
    except:
        break
a = sorted(a)
rank = 1
found = False
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        rank += 1
        if rank == 3:
            print(a[i])
            found = True
            break
if not found:
    print("-")


