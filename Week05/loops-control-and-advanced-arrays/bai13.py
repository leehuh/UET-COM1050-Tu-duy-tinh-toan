def tonguoc(n):
    sum = 0
    for uoc in range(1, n // 2 + 1):
        if n % uoc == 0:
            sum = sum + uoc
    return sum
m, n = map(int, input().split())
if tonguoc(m) == n and tonguoc(n) == m:
    print("true")
else:
    print("false")