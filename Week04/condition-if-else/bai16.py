def up(n):
    if n - int(n) == 0:
        return int(n)
    else:
        if n > 0:
            return int(n) + 1
        else:
            return int(n)
def down(n):
    if n - int(n) == 0:
        return int(n)
    else:
        if n > 0:
            return int(n)
        else:
            return int(n) - 1
def round(n):
    if n - int(n) == 0:
        return int(n)
    if n > 0:
        if abs(n - int(n)) < 0.5:
            return int(n)
        else:
            return int(n) + 1
    else:
        if abs(n - int(n)) < 0.5:
            return int(n)
        else:
            return int(n) - 1 
n = float(input())
print(up(n), down(n), round(n))