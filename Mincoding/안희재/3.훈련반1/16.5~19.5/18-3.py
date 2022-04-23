# 이건 2중배열을 dat에 넣는 문제네
bucket = [0] * 10 # 숫자는 1~9니까.

arr = []
for i in range(3):
    row = list(map(int,input().split()))
    arr.append(row)

for i in range(3):
    for j in range(3):
        index = arr[i][j]
        bucket[index] += 1

for i in range(1,len(bucket)): # 1부터임! 10칸 만들었잖아. (9칸 만들면, 12번째 줄에서 인덱스 오류남)
    if bucket[i] == 0:
        print(i, end = ' ')