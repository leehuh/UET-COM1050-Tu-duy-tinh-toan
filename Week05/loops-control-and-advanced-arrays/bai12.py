x = float(input())
n = int(input())
for _ in range(n):
    x = x + x * 0.7 / 100
print(int(x))