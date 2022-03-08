arr = [4,3,6,1,3,1,5,3]
num = int(input())

cnt = 0
for i in arr:
    if i == num:
        cnt += 1

print(f'숫자{num}개수는{cnt}개')