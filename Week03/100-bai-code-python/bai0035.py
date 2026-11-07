def is_prime(a):
    uoc = 1
    for i in range(1, a//2+1):
        if a % i == 0:
            uoc += 1
    if uoc == 2:
        return True
m, n = map(int, input().split())
s = 0
c = 0
for t in range(m, n + 1):
    if (is_prime(t)):
        s = s + t
        c = c + 1
print(f"{s/c:.2f}")
