arr = [list(input()) for _ in range(4)]


length = [0]*4
for i in range(4):
    length[i] = len(arr[i])


length = sorted(length)

print(*length, sep= ' ')