def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m
m, n = map(int, input().split())
a = gcd(m, n)
print(f"{m//a}/{n//a}")