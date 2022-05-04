# 연산 카드는 일단 모-두 써야 함 + "순열"
# 처음에 나누기는 //로 했는데 -> -2//3은 0(버림이니까)이되어야 하는데, -1이 되어버림
# 또한, Max를 처음에 0로 했음 -> 음수가 최댓값인 경우 당연히 0이 되어서 갱신이 안됨 ㅠ
# 가장 중요한것 : 시간초과로 실패 -> 10번케이스가 vsc에서도 1분넘게 걸림
    # 숫자 12개? -> 연산 11개 -> (11! / 2! / 6! / 2!)case임ㅋㅋ
    # 이제 무지성으로 코드 짤 때는 지난듯 하하

import sys
sys.stdin = open('숫자만들기_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    operator1 = list(map(int,input().split())) # 차례대로 '+','-','*','//'
    operator2 = ['+']*operator1[0] + ['-']*operator1[1] + ['*']*operator1[2] + ['/']*operator1[3]
    # 2 1 0 1면 -> [+, +, -, /] 
    numbers = list(map(int,input().split()))
    cnt = 0
    def dfs(level,result):
        global Min, Max, cnt
        if level == len(numbers)-1:
            if Min > result:
                Min = result 
            if Max < result:
                Max = result
            cnt += 1
            return

        for i in range(len(operator2)):
            if visit[i] == 0 and operator2[i] == '+':
                visit[i] = 1
                dfs(level+1,result+numbers[level+1])
                visit[i] = 0

            if visit[i] == 0 and operator2[i] == '-':
                visit[i] = 1
                dfs(level+1,result-numbers[level+1])
                visit[i] = 0

            if visit[i] == 0 and operator2[i] == '*':
                visit[i] = 1
                dfs(level+1,result*numbers[level+1])
                visit[i] = 0

            if visit[i] == 0 and operator2[i] == '/':
                visit[i] = 1
                dfs(level+1,int(result/numbers[level+1]))
                visit[i] = 0

    Min, Max = 2e18, -2e18
    visit = [0] * (N-1) # operator2만큼 칸 만듦
    dfs(0,numbers[0]) # 초기값
    print(f'#{tc}', Max-Min, cnt)