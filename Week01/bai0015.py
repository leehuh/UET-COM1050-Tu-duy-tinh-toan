from math import sqrt 

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a + b > c and b + c > a and c + a > b:
    cv = a + b + c
    p = cv / 2
    s = sqrt(p * (p - a) * (p - b) * (p -c))
    print("Day la 3 canh cua mot tam giac")
    print(f"{cv:.2f} {s:.1f}")
else:
    print("Day khong phai la 3 canh cua mot tam giac")