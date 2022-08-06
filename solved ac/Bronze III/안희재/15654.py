# 흔한 DFS -> 동일 수열은 배제 -> check배열 따로 만들어서 관리
# 빽트랙킹 필수

N, M = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()
# dfs인가?
check = [0] * N
result = []

def dfs(level):
    if level == M:
        print(' '.join(map(str, result))) # 여기 구현에서 애먹었음;; 너무 오랜만이었..
        return # 여기도;;
    
    for k in range(N):
        if check[k] == 0:
            check[k] = 1
            result.append(arr[k])
            dfs(level+1)
            result.pop() # 빽트랙킹
            check[k] = 0

dfs(0)