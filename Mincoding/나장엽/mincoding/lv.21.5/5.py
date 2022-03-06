arr = list(map(int, input().split()))

bucket = [0]*10
# 숫자의 등장횟수 표기하기
for i in range(len(arr)):
    bucket[arr[i]] += 1
    
counting_arr = [0]*10
#counting_arr은 누적합을 저장할 배열
counting_arr[0] = bucket[0]

#슷자의 등장횟수 누적합 구하기.
for k in range(1, 10):
    counting_arr[k] = counting_arr[k-1] + bucket[k]
    
result = [0]*9
#result 는 정렬된 결과를 저장하는 배열

for j in range(len(arr)-1, -1, -1):
    result[counting_arr[arr[j]]] = arr[j]
    counting_arr[arr[j]] -= 1
    
for l in range(1, len(result)):
    print(result[l], end=' ')