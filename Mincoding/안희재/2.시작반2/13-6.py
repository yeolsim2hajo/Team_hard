arr = [[4,5,6,1,3,1], [2,1,3,6,3,6]]

def Input():
    a, b, c = map(int,input().split())
    return a,b,c

def Process(tuple):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    for i in range(2):
        for j in range(6):
            if arr[i][j] == tuple[0]:
                cnt1 += 1
            if arr[i][j] == tuple[1]:
                cnt2 += 1
            if arr[i][j] == tuple[2]:
                cnt3 += 1
    return {tuple[0]:cnt1, tuple[1]:cnt2, tuple[2]:cnt3}

def Output(dict):
    print(f'{list(dict.keys())[0]}={list(dict.values())[0]}개')
    print(f'{list(dict.keys())[1]}={list(dict.values())[1]}개')
    print(f'{list(dict.keys())[2]}={list(dict.values())[2]}개')

def main():
    Output(Process(Input()))

main()