def isprime(n):
    p = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            p = p + 1
    if p == 2:
        return True
    return False
m, n = map(int, input().split())
c = 0
for t in range(m, n + 1):
    if isprime(t):
        c = c + 1
print(c)    
