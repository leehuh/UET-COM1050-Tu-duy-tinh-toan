def reverse(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
n = int(input())
step = 0
while n != reverse(n):
    n = n + reverse(n)
    step += 1
print(step, n)