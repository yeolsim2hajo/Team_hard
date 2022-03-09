arr = [['D','A','D'],['Q','W','Q'],['A','S','D'],['A','S','D']]

def main():
    word = input()
    return word

def find(x):
    result = '없음'
    for i in range(4):
        for j in range(3):
            if arr[i][j] == x:
                result = '존재'
                print(result)
                return
    print(result)
    return

find(main())