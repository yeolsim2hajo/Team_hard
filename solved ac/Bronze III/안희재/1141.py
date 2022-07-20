import sys

n = int(sys.stdin.readline())
words = [(sys.stdin.readline()).rstrip() for _ in range(n)]


words.sort(key=len)
res = 0


for i in range(n):
    flag = False
    for j in range(i + 1, n):
        if words[i] == words[j][0:len(words[i])]:
            flag = True
            break
    if not flag:
        res += 1

print(res)