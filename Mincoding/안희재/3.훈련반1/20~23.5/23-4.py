# 순열, S가 무조건 포함
n = int(input())
members = ['B','T','S','K','R']
path = [''] * n
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
        if level > 0 and (path[level-1] == members[i]):
            continue
        path[level] = members[i]
        abc(level+1)
        path[level] = ''

abc(0)
print(cnt)
# 아. 이렇게 하는게 아니지. 
# 이건 연속만 컷하는 코드.. used써야겠네