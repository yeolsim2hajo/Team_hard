arr = [1,2,3,3,5,1,0,1,3]
num = int(input())
# sliding window 알고리즘으로 풀어야 함

sum = 0
for i in range(num):
    sum += arr[i]
Min = sum

for i in range(len(arr)-num+1):
    if sum < Min:
        Min = sum
    if i == len(arr)-num:
        break # 여기를 넣어줘야지. 안 그러면 15번째 줄에서 index 초과 에러 남
    sum += arr[i+num]
    sum -= arr[i]

print(Min)
