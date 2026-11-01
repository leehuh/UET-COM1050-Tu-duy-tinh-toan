n = int(input())
c = 0
for i in range (1, n+1):
    if i % 3 == 0:
        print(i,end = " ")
        c += 1
    if c == 0:
        print("-")
    
