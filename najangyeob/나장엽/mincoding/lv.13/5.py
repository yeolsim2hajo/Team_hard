def main():
    lst = KFC()
    print(f'대문자{lst[0]}개')
    print(f'소문자{lst[1]}개')

def KFC():
    cnt_upper = 0
    cnt_lower = 0
    str = input()
    for i in range(len(str)):
        if ord('A') <= ord(str[i]) <= ord('Z'):
            cnt_upper += 1
        if ord('a') <= ord(str[i]) <= ord('z'):
            cnt_lower += 1
    lst = [cnt_upper, cnt_lower]
    return lst

main()