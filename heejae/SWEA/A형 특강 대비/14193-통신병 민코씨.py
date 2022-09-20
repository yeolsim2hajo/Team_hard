# 흠.. flood fill을 통한, bfs를 쓰되,
# 기본적으로 S를 향하되, 모든 A가 S로 연결되는 건 아님.
    # S로 가다가, 가까운 다른 A가 있다면 그거랑 연결!
    # 포문 돌려서, A만나면 bfs 돌림 -> 자기자신 먼저 침몰 및
        # 도중에 A만나면 그때의 레벨을 총 Sum변수에 추가시키고, 만난 A 침몰
        # 어.. 근데 고려해야 할 점이 좀 많네.. 아례 예 처럼
# 아니다. A를 딱 집으면 => 제일 가까운 A와 S와의 거리 -> 더 가까운 것과 연결.
# 즉, A의 선택지는 딱 3개뿐임 -> (1)다른 인접A or (2)S와 연결 or (3)둘다 연결된 상태
    # 아래 예시에서는 위아래의 AAA중에서 가운데 A가 S와 연결되는게 제일 비용 최소지
    # Final: 만약 처음부터 인근에 A없어서 S랑 연결되는게 더 빠르면 S연결해. 그럼 끝임. 
    # 골치아픈 경우는, A랑 연결된 경우임. 어쨋든 A그룹들 중 한명은 S랑 연결되어야 하기 때문에.

# BFS를 2개 만들든지 해서 총 2단계를 진행하자
    # Step1 - A끼리 그룹화
        # S보다 A먼저 만나면 C로바꾸고, 연결비용 Sum에 추가
            # 아냐, tmp배열에 각 좌표 추가시키고, 걍 '_'로 바꾸기
        # 만약, S를 먼저 만나면 0으로 바꾸고, 연결비용 Sum에 추가 (여기 정확한가? 논리에 오점은 없나?)
            # 흠.. 일단 근처에 A가없다는 뜻이니까, 괜찮을것같은데? 
        # 결국, 모든 A는 사라짐(C로 그룹화) => ㄴㄴㄴㄴ. 아냐. 한 그룹 만들면 S랑 연결 바로 시키자
            # 이 작업을 안하면, C들이 어떤 그룹끼리 묶여있는지 판단하기 힘듦
    # Step2 - 방금 만든 C그룹을 S랑 연결시키기. 
        # C그룹의 각 좌표들 중에서 S위치와 제일 가까운 것이 비용ㅇㅇ. abs(x-x1)+abs(y-y1)

# -----------------
#####__
#AAA###
#____A#
#_S_###
#_____#
#AAA###
#####__
# -----------------
from collections import deque
col, row = map(int,input().split()) # col가 열, row가 행
arr = [list(input()) for _ in range(row)]

for i in range(row):
    for j in range(col):
        if arr[i][j] == 'S':
            Sx, Sy = i, j # S의 좌표

def A_S(a,b): # A(a,b좌표인)와 S의 거리 판단하는 함수
    return abs(Sx-a)+abs(Sy-b)

# 걍 처음부터 솔로는 아예 전부 침몰 및 연결비용 추가시키고 시작하.
def A_A(a,b,level): # A(a,b좌표인)와 가장 가까운 A의 거리
    global result
    q = deque()
    q.append((a,b,level))

    while q:
        nowx,nowy, level = q.popleft()
        directx = [-1,1,0,0]
        directy = [0,0,-1,1]

        for i in range(4):
            dx = nowx+directx[i]
            dy = nowy+directy[i]
            if not(0<=dx<row and 0<=dy<col): continue
            if arr[dx][dy] == '#': continue
            if arr[dx][dy] == 'A': # 최초의 A = A중에서, 가장 근접한 A를 만났을 때
                if level+1 > A_S(a,b): # 그 거리가 처음A에서 S와의 거리보다 클 때: 처음A는 독립이란 뜻(외딴 무인도랄까나)
                    result += A_S(a,b)
                    return # 그리고 끝
                else:
                    arr[a][b] = 'A' # 첨에 침몰시킨거 부활
                    return # 아니면 그룹화해야할 것이기에, 침몰 x하고 return. 흠 아쉬운데 여기서 끝내기에..
            q.append((dx,dy,level+1))

result = 0
group_number = 1
for i in range(row):
    for j in range(col):
        if arr[i][j] == 'A':
            arr[i][j] = '_'
            A_A(i,j,0) # 이제, 솔로는 다 제거. 남은 A는 모두 그룹화시킬 것임.

# 와 유니온파인드 마지막에 쓰면 되네 이제
group = [[0]*col for _ in range(row)] # 여기에다 각 A들의 그룹정보를 답을 것

def union_bfs() # 계속 합병시키다가, 


# def bfs(x,y,level): # 이거 ㄴ게속 하는게 아님. 그냥 한번 S나 A만나면 바로 끝
#     global result, A_group
#     q = deque()
#     q.append((x,y,level))

#     while q:
#         nowx,nowy, level = q.popleft()
#         directx = [-1,1,0,0]
#         directy = [0,0,-1,1]

#         for i in range(4):
#             dx = nowx+directx[i]
#             dy = nowy+directy[i]
#             if not(0<=dx<row and 0<=dy<col): continue
#             if arr[dx][dy] == '#': continue
#             if arr[dx][dy] == 'A':
#                 if A_S(dx,dy) <= level+1: # 같은 경우는.. 상관없을듯 이렇게 일단 둬보자!
#                     arr[dx][dy] = 0 # 솔로는 S연결비용 추가시키고 침몰시키기!
#                     # 아 아아아아 일단 .그냥 솔로는 전부 침몰시키고 시작하자
#                     result += A_S(x,y)
#                     return
#                 else: # 즉, 근처 A가 S보다 가까우면,
#                     A_group.append(dx,dy)

#                     result += level+1 # A와 연결비용 추가
#                     return
#             # q.append ??


# result = 0
# for i in range(row):
#     for j in range(col):
#         if arr[i][j] == 'A':
#             A_group = []
#             arr[i][j] = 0 # 본인 침몰시키고 시작
#             # bfs(i,j,0)bfs 돌리고, A그룹에 추가시키기




