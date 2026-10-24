from math import sqrt
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

cv = a + b + c
p = cv / 2
s = sqrt(p * (p - a) * (p - b) * (p -c))

print(f"{cv:.1f} {s:.3f}")