member = ['B','T','S','K','R']
n = int(input())
path = ['']*n
used = [0]*5
cnt = 0
def abc(level):
    if level == n:
        global cnt
        for i in range(n):
            if 'S' in path[i]:
                cnt += 1
        return

    for i in range(5):
        if used[i] == 0:
            path[level] = member[i]
            used[i] = 1
            abc(level+1)
            path[level] = ''
            used[i] = 0
abc(0)
print(cnt)