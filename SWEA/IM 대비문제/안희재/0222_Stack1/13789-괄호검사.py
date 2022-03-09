T = int(input())

for tc in range(1,T+1):
    word = input()
    cnt_1 = 0 # {} -> {만나면 +1, }만나면 -1
    cnt_2 = 0 # ()

    for i in range(len(word)):
        if word[i] == '{':
            cnt_1 += 1
        elif word[i] == '}':
            cnt_1 -= 1
        elif word[i] == '(':
            cnt_2 += 1
        elif word[i] == ')':
            cnt_2 -= 1
        else:
            continue

    if cnt_1 != 0 or cnt_2 != 0:
        print(f'#{tc}', 0)
    else:
        print(f'#{tc}', 1)

# 아.. 이렇게 풀면 안된다..
# {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다
# 이 경우도 고려해 줘야지..