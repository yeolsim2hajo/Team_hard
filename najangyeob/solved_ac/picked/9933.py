# 그냥 문자열과 뒤집힌 문자열이 있으면 비밀번호

# 2중 for문으로 검사
N = int(input())

word = []
for _ in range(N):
    word.append(input())

length = 0
alpha = ''

for i in word:
    if i[::-1] in word:
        length = len(i)
        alpha = i[length//2]
        break
    
print(length, alpha)