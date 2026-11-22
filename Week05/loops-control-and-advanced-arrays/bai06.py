def isprime(n):
    count = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
a, b = map(int, input().split())
sum = 0
for num in range(a, b + 1):
    if isprime(num):
        sum = sum + num
print(sum)