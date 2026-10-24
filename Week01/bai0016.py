a, b = input().split()

a = float(a)
b = float(b)

tbcn = (a + b * 2) / 3
print(f"{tbcn:.1f}")
if tbcn >= 8:
    print("Gioi")
elif tbcn < 8 and tbcn >= 6.5:
    print("Kha")
elif tbcn < 6.5 and tbcn >= 5.0:
    print("Trung binh")
elif tbcn < 5 and tbcn >= 3.5:
    print("Yeu")
else:
    print("Kem")