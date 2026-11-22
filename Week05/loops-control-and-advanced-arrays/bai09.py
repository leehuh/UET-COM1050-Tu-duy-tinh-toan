def issquare(n):
    square = int(n ** 0.5)
    if square * square == n:
        return True
    return False
n = int(input())
count = 0
for num in range(1, n + 1):
    if issquare(num):
        print(num, end = " ")
        count = count + 1
    if count == 0:
        print("no number")
    