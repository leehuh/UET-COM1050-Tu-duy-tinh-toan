def ucln(m, n):
    for uoc in range(m - 1, 0, -1):
        if m % uoc == 0 and n % uoc == 0:
            return uoc
m, n = map(int, input().split())
print(ucln(m,n))