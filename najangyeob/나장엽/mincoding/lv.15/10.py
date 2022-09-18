

def main():
    arr = [list(input()) for _ in range(3)]
    countLine(arr)


def countLine(arr):
    result = []
    for i in range(len(arr)):
        result.append(len(arr[i]))
    
    for i in range(3):
        print('{0}='.format(result[i]), end='')
        print(*arr[i], sep='')
    # for i in range(3):
    #     print(*arr[i], sep='')

main()