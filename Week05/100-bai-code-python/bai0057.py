a = []
while True:
    try:
        a.append(int(input()))
    except:
        break
a_set = set(a)
print(len(a_set))