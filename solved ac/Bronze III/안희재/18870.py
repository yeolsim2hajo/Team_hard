a = input()
# 인덱싱
num = list(enumerate(list(map(int,input().split()))))
# 빈배열 만들기
lst = [0 for i in range(len(num))]
# 2차원 정렬
num.sort(key=lambda x:x[1])

# 빈 배열에 집어넣기
idx = -1
now = 0.5
for i in range(len(num)):
    if now != num[i][1]:
        idx += 1
        now = num[i][1]
        lst[num[i][0]] = idx
    else:
        lst[num[i][0]] = idx
print(*lst)