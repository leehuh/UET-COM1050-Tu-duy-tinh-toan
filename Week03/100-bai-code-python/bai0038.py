def is_prime(a):
    uoc = 1
    for i in range(1, a//2+1):
        if a % i == 0:
            uoc += 1
    if uoc == 2:
        return True
    
k = int(input())
i = 2
c = 0
while c < k:
    if (is_prime(i)):
        print(i,end=" ")
        c = c + 1
    i = i + 1