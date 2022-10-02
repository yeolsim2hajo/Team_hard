# deque로 푼 것은 똑같지만 // rstrip, enumerate 등을 사용하여 내 코드보다 더 직관적으로 코드 작성
# 참고링크:https://velog.io/@uoayop/BOJ-4485-%EB%85%B9%EC%83%89-%EC%98%B7-%EC%9E%85%EC%9D%80-%EC%95%A0%EA%B0%80-%EC%A0%A4%EB%8B%A4%EC%A7%80Python
import sys
from collections import deque
input = sys.stdin.readline

cnt = 0
while(1):
    n = int(input().rstrip()) # n: 동굴 크기(n*n)
    cnt += 1
    if n == 0 :
        break
    
    dx = [-1,1,0,0] # 상하좌우
    dy = [0,0,-1,1]

    map = [[0 for _ in range(n)] for _ in range(n)] 
    # thief: 각 위치에 따라 가장 적게 잃을 수 있는 루피 값을 비교해가면서 최소 값을 갱신하면서 입력
    theif = [[99999 for _ in range(n)] for _ in range(n)] # 99999 > 125 * 2 * 9 (최대 맵크기 125 / 제일 긴 줄 -> 곱하기2 / 모든 루피의 값은 9이하의 정수)
    visited = [[0 for _ in range(n)] for _ in range(n)] 

    # 공백 제거 -> enumerate로 인덱스와 값을 나누어서 map[i][j]에 값을 모두 배정
    # 본래 내 코드는 이 부분에서 더 길었다
    for i in range(n):
        row = (input().rstrip()).replace(' ','')
        for j,char in enumerate(row):
            if char != " ":
                map[i][j]=int(char)

    # bfs
    q = deque()
    q.append((0,0))
    theif[0][0] = map[0][0] 

    while q:
        i, j = q.popleft()
        visited[0][0] = 1 # 시작점의 초기값은 1 

        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n: # 범위 내
                if not visited[nx][ny]: # 재방문 방지
                    if theif[nx][ny] > theif[i][j] + map[nx][ny]: # 최소비용
                        theif[nx][ny] = theif[i][j] + map[nx][ny]
                        # 단, visited[nx][ny]에 1체크 ㄴㄴ -> 모든 경우의 수를 확인해야 하므로, 중간 경로가 중복될 수 있는 경우 체크
                        q.append((nx,ny))
    
    print("Problem {0}: {1}".format(cnt,theif[n-1][n-1]))