n = int(input())
members = ['B','T','S','K','R']
path = [''] * n
used = [0] * 5
cnt = 0

def abc(level):
    if level == n:
        for i in range(len(path)):
            if path[i] == 'S':
                global cnt
                cnt += 1
                return
        return

    for i in range(5):
        if used[i] == 1:
            continue
        path[level] = members[i]
        used[i] = 1
        abc(level+1)
        used[i] = 0

abc(0)
print(cnt)