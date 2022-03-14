def main():
    arr = [[''] * 10 for _ in range(3)]
    for i in range(3):
        word = input()
        for j in range(len(word)):
            arr[i][j] = word[j]

    countline(arr)

def countline(array):
    for i in range(3):
        a = ''.join(array[i])
        b = len(a)
        print(f'{b}={a}')

main()