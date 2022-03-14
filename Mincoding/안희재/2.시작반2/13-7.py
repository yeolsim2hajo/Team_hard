arr = [['A','D','F'],['Q','W','E'],['Z','X','C']]

def main():
    word = input()
    print(f'{find(word)[0]},{find(word)[1]}')

def find(target):
    x, y = 0,0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == target:
                x, y= i, j

    return x, y

main()