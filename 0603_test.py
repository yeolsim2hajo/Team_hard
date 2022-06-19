#1
def dfs(arg):
    print(arg,end=' ')
    if arg == 15:
        print(arg, end=' ')
        return
    dfs(arg+2)
    print(arg,end=' ')

dfs(3)


#2