from math import sqrt
def is_square(n):
    for i in range(int(sqrt(n))+1):
        if i**2 == n:
            return True
    return False

k = int(input())
i = 0
c = 0
while c < k:
    if (is_square(i)):
        print(i,end=" ")
        c = c + 1
    i = i + 1