str = input()
arr = [i for i in str]

# 0 1 2 3 4 / 4 3 2 1 0

def bbq(level):
    print(arr[level], end= '')
    if level == 4:
        print()
        print(arr[level], end= '')
        return

    bbq(level+1)
    print(arr[level], end= '')

bbq(0)