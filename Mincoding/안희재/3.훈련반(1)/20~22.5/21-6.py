branch, level = map(int,input().split())

cnt = 0
def abc(depth):
    global cnt
    cnt += 1
    if depth == level:
        return

    for i in range(branch):
        abc(depth+1)


abc(0) # depth(level)
print(cnt)
