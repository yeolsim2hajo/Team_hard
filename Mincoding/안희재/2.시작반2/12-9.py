word = input()

if ord(word) <= 57: # 문자형 숫자
    arr = [[' '] * 3 for _ in range(3)]
    tmp = 6
    for i in range(3):
        for j in range(3-i):
            arr[i][i+j] = tmp
            tmp -= 1
else:
    arr = [[' '] * 3 for _ in range(3)]
    tmp = 1
    for i in range(3):
        for j in range(0,3-i):
            arr[2-i][j] = tmp
            tmp += 1

for i in range(3):
    print(*arr[i],sep='')
