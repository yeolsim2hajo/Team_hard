vect = [[3,7,4], [2,2,4], [2,2,5]]
target = input().split()

for k in range(len(target)):
    cnt = 0
    max = 0
    max_str = ''
    for i in range(3):
        for j in range(3):
            if k == vect[i][j]:
                cnt += 1
    if max < cnt:
        max = cnt
        max_str = k

print(max_str)

# 어 음.. 이건 내가 전에 풀어본 유형이라 금방 푼 듯..