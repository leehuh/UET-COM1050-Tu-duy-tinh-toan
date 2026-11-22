n = abs(int(input()))
count = 1
while n >= 10:
    count += 1
    n = n // 10
print(count)