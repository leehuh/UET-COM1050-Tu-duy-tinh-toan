n = int(input())
collatz_len = []
for x in range(1, n+1):
    length = 1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            length += 1
        else:
            x = x * 3 + 1
            length += 1
    collatz_len.append(length)
max_index = 0
for i in range(len(collatz_len)):
    if collatz_len[i] > collatz_len[max_index]:
        max_index = i
print(max_index + 1, collatz_len[max_index])