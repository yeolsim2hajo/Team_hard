# 시간 초과 해결법
    # 와 진짜; 개쩌네. 나같은 경우 10번케이스: 11!/2!/1!/6!/2!인데
        # 어라 아닌데. 레퍼런스가 11!/2!/1!/6!/2! 나오는 거임!
            # +가 2개일때 내 코드는 +(1),+(2) / +(2),+(1) 이 2개를 모두 세게 됨 ㅠㅠ
            # 2!, 1!, 6!, 2! 는 +가 2개인경우 -> 이 코드는 중복과정을 제거해줌!
        # 나는 순열로 풀었음 -> 답은 나오지만, 빽트랙킹 과정이 필요함!!
            # 1트와 레퍼런스에 cnt변수 넣어서 세는 횟수 체크가능함
    # 똑같은 결과는 굳이 쓸 필요가 없잖아
    # 이렇게 하면 그냥 브랜치4개만 뻗어나가면 되잖아;
        # 또한, 그냥 if문 4개로 연결했음. wow;
    # 난 끽해야 재방문방지 하나 만들어놓았을뿐;;
    

import sys
sys.stdin = open('숫자만들기_input.txt','r')

def dfs(level,result):
    global Min, Max, cnt
    if level == len(numbers)-1:
        if Min > result:
            Min = result 
        if Max < result:
            Max = result
        cnt += 1
        return

    # 여기서는 각 연산자가 여러개 나오든 그걸 일일이 다른 문자로 생각해서 세주지 않음..
        # 이게 가장 큰 차이 ㅠ
    if visit[0] != operator[0]:
        visit[0] += 1
        dfs(level+1,result+numbers[level+1])
        visit[0] -= 1

    if visit[1] != operator[1]:
        visit[1] += 1
        dfs(level+1,result-numbers[level+1])
        visit[1] -= 1

    if visit[2] != operator[2]:
        visit[2] += 1
        dfs(level+1,result*numbers[level+1])
        visit[2] -= 1

    if visit[3] != operator[3]:
        visit[3] += 1
        dfs(level+1,int(result/numbers[level+1]))
        visit[3] -= 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operator = list(map(int,input().split())) # 차례대로 '+','-','*','//'
    numbers = list(map(int,input().split()))
    cnt = 0
    Min, Max = 2e18, -2e18
    visit = [0] * 4 
    dfs(0,numbers[0]) # 초기값
    print(f'#{tc}', Max-Min, cnt)