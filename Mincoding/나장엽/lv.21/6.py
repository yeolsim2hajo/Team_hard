branch, level = map(int, input().split())


# 재귀함수가 호출되는 횟수를 카운팅
cnt = 0
def abc(lv):
    global level
    global branch
    global cnt
    cnt += 1
    if lv == level:
        return cnt

    for i in range(branch):

        abc(lv+1)

abc(0)

print(cnt)
