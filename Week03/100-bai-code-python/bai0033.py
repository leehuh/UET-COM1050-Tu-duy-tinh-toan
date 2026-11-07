m, n = map(int, input().split())
t = 0
p = 1
c = 0
for i in range(n - m + 1):
    t = m + i
    for j in range(1, t//2+1):
        if t % j == 0:
            p = p + 1 
    if p == 2:
        c = c + 1
    p = 1
print(c)    