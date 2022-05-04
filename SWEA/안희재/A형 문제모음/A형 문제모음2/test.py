import sys
sys.stdin = open('숫자만들기_input.txt','r')
def dfs(level, sum):
    global max, min
    if level == N - 1: # level이 N-1이 될때 리턴
        if sum > max:
            max = sum
        if sum < min:
            min = sum
        return
    if visit[0] != value[0]: # 연산자를 얼마나 썼는지 비교
        visit[0] += 1 # visit의 '+' 값에 + 1
        dfs(level + 1, sum + arr[level + 1]) # sum에 arr[level+1] 더하기
        visit[0] -= 1 # return 되면 +연산자를 쓴게 아니니까 -1
    if visit[1] != value[1]:
        visit[1] += 1
        dfs(level + 1, sum - arr[level + 1])
        visit[1] -= 1
    if visit[2] != value[2]:
        visit[2] += 1
        dfs(level + 1, sum * arr[level + 1])
        visit[2] -= 1
    if visit[3] != value[3]:
        visit[3] += 1
        dfs(level + 1, int(sum / arr[level + 1])) # -2/3 은 -0.6666, -2//3 은 -1이 나오므로 int()해주기
        visit[3] -= 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    value = list(map(int, input().split()))  # + - * / 갯수
    visit = [0] * len(value) # 어떤 연산자를 얼마나 썼는지 기록할 배열
    arr = list(map(int, input().split())) # 숫자 배열
    max = -21e8
    min = 21e8
    dfs(0, arr[0]) # level, sum
    print(f'#{tc} {max - min}')