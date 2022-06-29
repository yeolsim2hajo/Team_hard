# 요세푸스 문제
# N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K가 주어진다.
# 순서대로 k번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# N명이 모두 제거 될 때까지 계쏙된다.
# 사람들이 제거되는 순서를 (N, K)-요세푸스 순열.


N, K = map(int, input().split())
que = [str(i) for i in range(1, N + 1)]

answer = []
idx = 0
while que :
    idx += K - 1 # 2, 4, 6, 8, 10, 12, 14
    if idx >= len(que): # 7 6 5 4 3 2 1 0
        idx = idx%len(que)
    answer.append(que.pop(idx)) # 3, 6, 2, 


print("<" + ', '.join(answer) + ">")

