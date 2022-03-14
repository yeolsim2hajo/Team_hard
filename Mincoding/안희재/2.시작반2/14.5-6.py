def main():
    arr = [[' '] * 3 for _ in range(3)]
    output(magic(arr))

def magic(array):
    tmp = 1
    for i in range(3):
        for j in range(i,3):
            array[i][j] = tmp
            tmp += 1
    return array

def output(x):
    for i in range(3):
        print(*x[i],sep='')

main()