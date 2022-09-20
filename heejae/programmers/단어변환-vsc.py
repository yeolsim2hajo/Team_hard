# 최소 -> bfs
from collections import deque

begin, target = input().split()
words = input().split() # hot dot dog lot log


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
            if cnt == 2:  # ㅆㅂㅋㅋ장난하냐? 단어 길이가 3일때만 되잖아 이거 ㅋㅋㅋ
                q.append((word,level+1))

if not target in words: print(0)
else:
    print(bfs(begin,0))


# hit cog
# hot dot dog lot log cog