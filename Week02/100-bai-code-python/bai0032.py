a, b = input().split()
a = int(a)
b = int(b)
t = 0
c = 0
s = 0
for i in range(b-a+1):
    t = a + i
    if t % 3 == 0 or t % 5 == 0:
        c = c + 1
    if t % 2 == 0:
        s = s + t
print(f"{c} {s}")

