arr = [[1,0,0,0,0], [1,0,1,0,0], [1,1,0,1,0], [1,0,1,0,0], [0,1,0,0,1], [0,0,0,1,0], [1,1,0,0,0]]

def Input():
    num = int(input())
    return num

def Process(x):
    cnt = 0
    for i in range(7):
        if arr[i][x] == 1:
            cnt += 1
    return cnt

def Output(x):
    print(x)

def main():
    Output(Process(Input()))

main()
