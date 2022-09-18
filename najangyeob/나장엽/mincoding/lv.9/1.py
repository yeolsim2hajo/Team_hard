arr = [4,3,6,1,3,1,5,3]
n = int(input())
cnt = 0

for i in range(len(arr)):
    if arr[i] == n:
        cnt += 1
        
print(f'숫자{n}개수는{cnt}개')