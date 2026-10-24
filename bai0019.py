s = input()

tong = sum(int (c) for c in s if c.isdigit())
nut = tong % 10
print(nut)

if nut == 9:
    print("may man")
else:
    print("chua may man")