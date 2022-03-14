arr = ['M','I','N','Q','U','E','S','T']

def Length(str):
    idx = 0
    for i in range(len(arr)):
        if arr[i] == str:
            idx = i
    return idx

def main():
    str1 = input()
    str2 = input()
    str3 = input()

    print(f'{str1}={Length(str1)}')
    print(f'{str2}={Length(str2)}')
    print(f'{str3}={Length(str3)}')


main()