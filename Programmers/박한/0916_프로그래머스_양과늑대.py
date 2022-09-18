# 프로그래머스 양과 늑대

from collections import deque

def solution(info, edges):
    arr = [[] for _ in range(len(info))]
    answer = 0
    for e in edges:
        arr[e[0]].append(e[1])
    q = deque([[0, 1, 0, set()]])
    while q:
        a, sheep, wolf, sett = q.popleft()
        if sheep > answer:
            answer = sheep
        sett.update(arr[a])
        for s in sett:
            if info[s]:
                if wolf != sheep-1:
                    q.append([s, sheep, wolf+1, sett-{s}])
            else:
                q.append([s, sheep+1, wolf, sett-{s}])
    return answer