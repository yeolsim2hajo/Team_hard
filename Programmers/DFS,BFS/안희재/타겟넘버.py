def solution(numbers, target):
    # n개의 정수들 -> n개의 연산자 존재(및 + or -) 
    # level은 n, branch는 2개
    answer = 0
    def dfs(level, Sum, target):
        nonlocal answer
        if level == len(numbers):
            if Sum == target:
                answer += 1
            return
        
        for i in range(2):
            if i == 0:
                dfs(level+1, Sum+numbers[level]*1, target)
            else:
                dfs(level+1, Sum+numbers[level]*(-1), target)
    
    dfs(0,0, target)
    
    return answer