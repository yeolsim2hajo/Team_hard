index = int(input())
arr = [3,7,4,1,9,4,6,2]

def abc(level, idx):
    global index
    print(arr[idx], end= ' ')
    if level == 0:
        return

    abc(level-1, idx-1)
    print(arr[idx], end= ' ')
abc(index, index)