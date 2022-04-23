def main():
    arr = [[0]*3 for _ in range(3)]
    Magic(arr)

def Magic(arr):
    n = 1
    for i in range(3):
        for k in range(i, 3, 1):
            arr[i][k] = n
            n += 1
    output(arr)

def output(arr):
    for i in range(3):
        for k in range(3):
            if arr[i][k] == 0:
                print(' ', end='')
            else: print(arr[i][k], end='')
        print()

main()
