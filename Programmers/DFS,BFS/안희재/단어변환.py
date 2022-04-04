# 프로그래머스 제출용 코드
from collections import deque

def solution(begin, target, words):
    answer = 0

    def bfs(start,level):
        q = deque()
        q.append((start,level))

        while q:
            now, level = q.popleft()
            if now == target:
                return level

            for word in words:
                if now == word: continue # 전하고 똑같으면 할 필요가 없지
                cnt = 0
                for i in range(len(word)):
                    if now[i] == word[i]: cnt += 1
                if cnt == len(word)-1: 
                    q.append((word,level+1))

    if not target in words: return answer
    else:
        answer = bfs(begin,0)
        return answer