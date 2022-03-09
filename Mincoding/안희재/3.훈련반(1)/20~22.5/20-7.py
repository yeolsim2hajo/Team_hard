arr = [3,7,4,1,9,4,6,2]
num = int(input())
# 3이면 -> 3 2 1 0 1 2 3 (인덱스)


def bbq(level):
    if level == 0:
        print(arr[level], end= ' ')
        return

    print(arr[level], end= ' ')
    bbq(level-1)
    print(arr[level], end= ' ')



bbq(num)
