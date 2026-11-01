n = int(input())
c = 1

for i in range(1, n//2):
    if n % i == 0:
        c = c + 1
print(c)