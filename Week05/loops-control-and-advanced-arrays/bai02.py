def isprime(n):
    count = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
while True:
    n = int(input())
    if n > 0:
        break
print(isprime(n))

