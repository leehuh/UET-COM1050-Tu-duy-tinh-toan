from math import sqrt
def is_square(n):
    for i in range(int(sqrt(n))+1):
        if i**2 == n:
            return True
    return False
n = int(input())
if (is_square(n)):
    print("Yes")
else:
    print("No")