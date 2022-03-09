arr = [['D','A','C','C','D'], ['S','D','F','A','E'], ['E','E','T','J','H']]

def main():
    Input()

def Input():
    word = input()
    if check(word):
        print('있음')
    else:
        print('없음')

def check(x):
    result = 0
    for i in range(3):
        for j in range(5):
            if arr[i][j] == x:
                result = 1
                return result
    return result

main()