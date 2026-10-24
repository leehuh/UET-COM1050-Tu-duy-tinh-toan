from math import sqrt
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

p = (a + b + c) / 2
s = sqrt(p * (p - a) * (p - b) * (p -c))

print(f"{(a * b * c)/(4 * s):.3f}")