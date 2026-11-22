con, chan = map(int, input().split())
for ga in range(con + 1):
    cho = con - ga
    if ga * 2 + cho * 4 == chan:
        print(ga, cho)
        break
else:
    print("invalid")