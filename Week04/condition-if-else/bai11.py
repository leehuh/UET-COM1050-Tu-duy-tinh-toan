a, b, c = map(int, input().split())
if a < b + c and b < c + a and c < a + b:

    if a == b == c:
        print("Tam giác đều")
    elif a == b or b == c or c == a:
        print("Tam giác cân")
    else:
        print("Tam giác thường")
else:
    print("Không phải tam giác")