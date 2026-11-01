a, b = input().split()
a = int(a)
b = int(b)
t = 0
c = 0
for i in range(b-a+1):
    t = a + i
    if t % 3 == 0:
        c = c + 1
print(c)