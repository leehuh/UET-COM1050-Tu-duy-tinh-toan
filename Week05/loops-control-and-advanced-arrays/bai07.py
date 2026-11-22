def isprime(n):
    count = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
n = int(input())
for i in range(n, 0, -1):
    if n % i == 0 and isprime(i):
        print(i)
        break