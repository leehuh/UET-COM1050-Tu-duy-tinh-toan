n = int(input())

if n <= 50:
    s = n * 600
    print(s)
elif n > 50 and n <= 100:
    s = 50*600 + (n - 50)*800
    print(s)
elif n > 100 and n <= 200:
    s = 50*600 + 50*800 + (n - 100)*1100
    print(s)
else:
    s = 50*600 + 50*800 + 100*1100 + (n - 200)*1500
    print(s)