def dfs(lst,number,arg=0,total=0):
    global answer
    if arg == len(lst):
        if total == number:
            answer += 1
        return
    dfs(lst,number,arg+1,total-lst[arg])
    dfs(lst,number,arg+1,total+lst[arg])

def solution(numbers, target):
    global answer
    answer = 0
    num_sum = sum(numbers)
    if num_sum > target:
        dfs(numbers,target)
    elif num_sum == target:
        answer = 1
    return answer