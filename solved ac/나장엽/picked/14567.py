# 선수과목 조건
# 선수과목 조건을 지킬 경우 각각의 전공과목을 언제 이수 할 수 있는지 궁금

# 한 학기에 들을 수 있는 과목 수에는 제한 없음
# 모든 과목은 매 학기 항상 개설된다.

# 모든 과목에 대해 각 과목을 이수하려면 최소 몇 학기가 걸리는지 계산하는 프로그램을 작성하라

# 과목수 n , 조건의 수 m 
# 선수과목 조건은 m개의 줄에 걸쳐 한 줄에 정수 a, b 형태로 주어진다.
# a번 과목이 b번 과목의 선수과목이다. 
# a < b인 입력만 주어진다
# 1 <= a < b <= n


# 위상정렬 :  순서가 정해져 있는 작업을 차례로 수행해야 할 때 그 순서를 결정하기 위해 사용하는 알고리즘
# 선수과목을 이수해야만 전공과목을 이수하기 때문에 위상정렬을 사용하기 좋음.
# https://m.blog.naver.com/ndb796/221236874984
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [1] * (n + 1) # [1, 1, 1, 1]
arr = [[] for _ in range(n+1)] # [ [], [], [], [] ]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(1, n + 1): # 1번 과목부터 시작하기때문에 1 ~ n + 1
    for k in arr[i] :
        graph[k] = max(graph[k], graph[i] + 1) # 

print(*graph[1:])
    