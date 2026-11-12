a, b, c = [int(input()) for _ in range(3)]
if a + b > c and b + c > a and a + c > b:
    print("Yes")
else:
    print("No")