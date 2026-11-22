n = int(input())
ds = list(map(int, input().split()))[:n]
found = False
for x in ds:
    if x == 42:
        found = True
        break
if found:
    print("I've found the meaning of life!")
else:
    print("It's a joke!")