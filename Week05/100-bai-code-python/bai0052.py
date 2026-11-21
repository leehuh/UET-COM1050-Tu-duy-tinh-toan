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
tbc = sum(prime_lst) / len(prime_lst)
if tbc == 0:
    print("-")
else:
    print(f"{tbc:.2f}")