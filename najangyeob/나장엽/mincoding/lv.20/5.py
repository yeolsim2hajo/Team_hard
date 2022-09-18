arr = list(input())


def abc(level, idx):
    print(arr[idx], end='')
    if level == 4:
        print()
        print(arr[idx], end='')
        return
    abc(level+1, idx+1)
    print(arr[idx], end='')


abc(0,0)