# 5지 선다 객관식 10문제
# 모든 문제를 찍음
# 3개의 연속된 문제의 답은 같게 하지 않는다!
# 영재가 5점일 경우의 수를 구하라.
# 1문제 당 1점
# [입력] -> 문제의 답이 입력으로 주어진다
# 1 2 3 4 5 1 2 3 4 5




# 설계
# 5 ~ 10점 까지 가능한 경우의 수를 구하기
# 모든 문제의 답을 다 골랐다면? 점수를 카운트하는 dfs
def dfs(solve):
    global choice, cnt

    if solve == 10: # 모든 문제를 다 풀었을때!
        score = 0

        for i in range(0, 10):
            if answer[i] == choice[i]: # 입력값인 답과, 선택한 답이 같으면
                score += 1 # 점수 1 증가

        if score >= 5: # 점수가 5점 이상인 경우
            cnt += 1 # 경우의 수 1 증가
        return

    for i in range(1, 6): # 5지 선다 이기때문에 1 ~ 5로 제한
        if solve > 1 and choice[solve - 1] == choice[solve - 2] == i: # 연속된 3개의 답은 같지 않게 선택함 # 2문제 이상 푼 경우 이전의 2 문제와 답이 같다면 continue
            continue
        choice.append(i)# 답 선택 # choice[solve] = i
        dfs(solve+1) # 재귀
        choice.pop()# 초기화 # choice[solve] = 0



answer = list(map(int, input().split()))
choice = []
# choice = [0]*len(answer)
cnt = 0
dfs(0)
print(cnt)






