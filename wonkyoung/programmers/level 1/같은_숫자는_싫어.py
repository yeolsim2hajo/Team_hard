# 220917
def solution(arr):
    answer = [arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer

def solution(arr):
    num = arr[0]
    answer = [num]
    for i in range(1,len(arr)):
        if arr[i] != num:
            answer.append(arr[i])
            num = arr[i]
    return answer