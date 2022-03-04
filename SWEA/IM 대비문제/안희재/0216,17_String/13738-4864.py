T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()

    for i in range(len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            print(f'#{tc} 1')
            break
    else:
        print(f'#{tc} 0')
    