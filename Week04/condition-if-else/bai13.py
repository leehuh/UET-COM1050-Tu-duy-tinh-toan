sodien = int(input())
if sodien <= 50:
    tiendien = 1500 * sodien
elif sodien <= 100:
    tiendien = 1500 * 50 + 2000 * (sodien - 50)
else:
    tiendien = 1500 * 50 + 2000 * 50 + 3000 * (sodien - 100)
print(tiendien)