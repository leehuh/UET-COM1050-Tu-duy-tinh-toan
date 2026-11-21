def isprime(n):
    count = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
ds = list(map(int, input().split()))
sum = 0
for num in ds:
    if isprime(num):
        print(num, end = " ")
        sum = sum + num
print()
if sum == 0:
    print("-")
else:
    print(sum)   

