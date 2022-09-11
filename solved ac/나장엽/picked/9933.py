# 그냥 문자열과 뒤집힌 문자열이 있으면 비밀번호

# 2중 for문으로 검사
N = int(input())

word = []
for _ in range(N):
    word.append(input())

for i in range(N):
    for k in range(1, N):
        if len(word[i]) == len(word[k]) and word[i][::-1] == word[k]:
            print(len(word[i]), word[i][int(len(word[i])/2)])