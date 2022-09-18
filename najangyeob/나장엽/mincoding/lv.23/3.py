arr =  ['A', 'B', 'C']
n = int(input())
path= ['']*n
cnt = 0

def abc(level):
    if level == n:
        global cnt
        cnt += 1
        return
    for i in range(3):
        if level > 1 and path[level-2] == arr[i] and path[level-1] == arr[i]:
            continue
        path[level] = arr[i]
        abc(level+1)
        path[level] = ''

abc(0)
print(cnt)