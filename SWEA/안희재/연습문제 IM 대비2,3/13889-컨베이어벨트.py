# N, K
# 길이가 2N인 버켓 만들고, 각각 내구도를 넣는다
# 3, 2 / 1 2 1 2 1 2 
# bucket = [1,2,1,2,1,2]
# 로봇이 지나갈때마다 -1
# 단계. 로봇추가(동시에 1번칸 내구도 깍기)
# 1단계. 벨트가 전체적으로 이동
# 2단계. 로봇 자체적으로 이동(이동할 수 있으면, 없으면으로 구분)
    # 단, 앞칸에 로봇없거나, 내구도가 있어야함
    # 로봇있고, 내구도가 없다면? : 벨트 이동만 기다려야 함
# 이 step1,2를 계속 반복하는거지 순서대로. while : 내구도 한계 달할때까지
    # 로봇추가는 1번 내구도가 0이 될때까지 추가
    # 끝까지 가면, 그 다음 이동은 처음으로.
# (1)now = ['','','','','',''] -> 로봇 올라타면 r
# (2)now = ['r', ...]
# (3)now = ['','r', ...]

N, K = map(int,input().split())
# [1,2,1,2,1,2] / 3, 2
life = list(map(int,input().split()))
stack = [''] * (2*N)
while (1):
    # 3단계(처음엔 로봇 없으니까 로봇추가부터)
    if life[0] != 0 and stack[0] != 'r': # 1번칸 내구도가 0이 아니고 비어있다면, 로봇추가
        stack[0] = 'r'
        life[0] -= 1
        if life.count(0) >= K:
            answer = 3 # 3단계
            break
    # 1단계(벨트 전체 이동)
    tmp = stack[len(stack)-1]
    for i in range(len(stack)-1,0,-1):
        stack[i] = stack[i-1]
    stack[0] = tmp
    # 이동 시킨 후에, 로봇(stack)있는 칸의 내구도(life) 깍기
    for i in range(len(stack)):
        if stack[i] == 'r':
            life[i] -= 1
    if life.count(0) >= K:
        answer = 1 # 1단계
        break
    # 2단계(로봇 자체 이동)
    stack_2 = [''] * (2*N) # 매번, 빈 배열로 초기화
    for i in range(len(stack)-1):
        if stack[i] == 'r' and stack[i+1] == '' and life[i+1] != 0:
            stack_2[i+1] = 'r'
            life[i+1] -= 1
        elif stack[i] == 'r':
            stack_2[i] = 'r' # 이동 안했으니, 라이프는 그대로
    # 마지막 경우 따로 뺐음        
    if stack[-1] == 'r' and stack[0] == '' and life[0] != 0:
        stack_2[0] = 'r'
        life[0] -= 1
    else:
        stack_2[-1] = 'r'
    
    stack = stack_2 # 갱신

    if life.count(0) >= K:
        answer = 2
        break

print(answer)
