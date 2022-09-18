def main():
    n = int(input())
    return n
def run(n):
    arr = [[0]*3 for _ in range(3)]
    a = 1
    if n < 10:
        for i in range(3):
            for k in range(3):
                arr[i][k] = a
                a += 1
    if n >= 10:
        for i in range(3):
            for k in range(2, -1, -1):
                arr[i][k] = a
                a += 1
    for i in range(3):
        print(*arr[i], sep ='')


run(main())