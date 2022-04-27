# NNNASBBSNV : 이 경우 3이 아니라 4임 -> NANV ! # 반복문자는 2개씩만 지워지니까

# 처음 버블식으로 쭉 순회하다, 찾으면 그거지우고 문자열 새로 담음.
# 다시 처음부터 찾는 식으로
# 언제까지? 없을때 까지

# for i in range(len(word)-2): # ABCCB -> word[3], wrod[3+1]까지만 볼거니까
#     if word[i] == word[i+1]:
#         word = word[i+2:]
#         break
#     # .. 음.. 그냥 while문으로 하는게 나을듯

T = int(input())

for tc in range(1,T+1):
    word = list(input())

    while (1):
        for i in range(len(word)-1): 
            if word[i] == word[i+1]:
                word = word[0:i]+word[i+2:]
                break
        else: # 발견되지 않는다면
            break
# for - else문 : 반복문 끝까지 돌린 경우에 else문 실행
    print(f'#{tc}', len(word))

