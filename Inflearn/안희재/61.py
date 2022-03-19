word = input()
result = ''
cnt = 0
tmp = word[0]

for i in range(len(word)):
    if word[i] == tmp:
        cnt += 1
    else:
        result += tmp + str(cnt)
        tmp = word[i]
        cnt = 1 
result += tmp + str(cnt)
# aaabbbbcdddd의 경우, idx가 끝이면 반복문에서는 추가 안하니까
# 따로 여기서 마지막으로 남은 잔재들 털어줘야 함
# ㄷㄷ;; 괜찮은데 이 스킬도????

print(result)