# dfs(brute force) / 단, 제한사항: 연속 3개의 답 같지 않도록
# 시간초과
def abc(level):
    global cnt
    if level == 10:
        score = 0
        for j in range(10):
            if array[j] == answers[j]:
                score += 1
        if score >= 5:
            cnt += 1
        return
    
    for i in range(1, 6): # 답: 1,2,3,4,5
        if level > 1 and array[level-2] == array[level-1] == i:
            continue
        array.append(i)
        abc(level+1)
        array.pop() # 원상복구
        
answers = list(map(int, input().split()))
array, cnt = [], 0

abc(0)
print(cnt)
# -----------------------------------

