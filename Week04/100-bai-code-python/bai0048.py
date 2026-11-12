n = int(input())
a = list(map(int, input().split()))
s = 0
c = 0
for i in range(n):
    if a[i] % 5 == 0:
        c = c + 1
        print(a[i], end = " ")
        s = s + a[i]
if c == 0:
    print("-")
else:
    print()
print(s)