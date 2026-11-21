a = list(map(int, input().split()))
max = None
for num in a:
    if num < 0:
        if max is None or num > max:
            max = num
if max is None:
    print("-")
else:
    print(max)