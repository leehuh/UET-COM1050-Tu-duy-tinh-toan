def is_square(n):
    if n < 0:
        return False
    can_n = int(n**0.5)
    if can_n * can_n == n:
        return True
    return False
a = list(map(int, input().split()))
sum = 0
count = 0
for x in a:
    if is_square(x):
        sum = sum + x
        count += 1
print(f"{sum / count}")