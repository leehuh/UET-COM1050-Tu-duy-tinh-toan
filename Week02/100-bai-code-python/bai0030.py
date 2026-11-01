a, b = input().split()
a = int(a)
b = int(b)
s = 0
for i in range(b-a+1):
    s = s + a + i
print(s)