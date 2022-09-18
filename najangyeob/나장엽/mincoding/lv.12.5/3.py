arr = [['D','A','D'],['Q','W','Q'],['A','S','D'], ['A','S','D']]

def main():
    str = input()
    find(str, arr)

def find(str, arr):
    flag = 0
    for i in range(len(arr)):
        for k in range(len(arr[i])):
            if arr[i][k] == str:
                flag = 1
    if flag:
        print('존재')
    else:
        print('없음')

main()