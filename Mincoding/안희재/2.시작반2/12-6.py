arr = ['M','I','N','Q','U','E','S','T']

def Length(x):
    idx = 0
    for i in range(len(arr)):
        if arr[i] == x:
            idx = i
    return idx

def main():
    a = input()
    b = input()
    c = input()
    print(f'{a}={Length(a)}')
    print(f'{b}={Length(b)}')
    print(f'{c}={Length(c)}')

main()