n = int(input())

a = n // 5000
b = (n - a*5000)//2000
c = (n - a*5000 - b*2000)//1000

print(a, b, c)