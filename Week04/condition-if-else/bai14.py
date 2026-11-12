a = float(input())
b = float(input())
if a == 0:
    if b == 0:
        print("Vô số nghiệm")
    else:
        print("Vô nghiệm")
else:
    print(f"{-b/a:.2f}")