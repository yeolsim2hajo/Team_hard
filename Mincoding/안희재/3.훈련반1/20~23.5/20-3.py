arr = list(map(int,input().split()))
# idex : 0 1 2 3 4 5 4 3 2 1 0

def bbq(level):
    if level == 5:
        print(arr[level], end = ' ')
        return
    
    print(arr[level], end = ' ')

    bbq(level+1)
    print(arr[level], end = ' ')

bbq(0)