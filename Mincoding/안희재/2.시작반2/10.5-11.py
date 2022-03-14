def main():
    num = int(input())
    return num

def run(x):
    arr = [[0] * 3 for _ in range(3)]
    if x < 10:
        tmp = 1
        for i in range(3):
            for j in range(3):
                arr[i][j] = tmp + j
            tmp += 3
    else:
        tmp = 3
        for i in range(3):
            for j in range(3):
                arr[i][j] = tmp - j
            tmp += 3
    for i in range(3):
        print(*arr[i],sep='')

run(main())
