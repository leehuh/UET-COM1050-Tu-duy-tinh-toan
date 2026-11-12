a, b, c, d = map(int, input().split())
if a != 0 and b % a == 0:
    q = b //a
    if b * q == c and c * q == d:
        print("YES")
    else:
        print("NO")
else:
    if a == b == c == d == 0:
        print("YES")
    else:
        print("NO")
