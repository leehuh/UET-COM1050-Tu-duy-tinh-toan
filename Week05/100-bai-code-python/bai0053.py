def isprime(n):
    count = 1
    for i in range(1, n//2 + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False
ds = list(map(int, input().split()))
prime_lst = []
for num in ds:
    if isprime(num):
        prime_lst.append(num)
max = prime_lst[0]
for num in prime_lst:
    if num > max:
        max = num
if len(prime_lst) == 0:
    print("-")
else:
    print(max)