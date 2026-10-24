a, b = input().split()

a = int(a)
b = int(b)

if a == 2:
    if (b % 400 == 0) or (b % 4 == 0 and b % 100 !=0):
        print("29")
    else:
        print("28")
elif a in (4, 6, 9, 11):
    print("30")
else:
    print("31")