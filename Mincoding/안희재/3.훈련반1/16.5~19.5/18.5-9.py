str = list(input())

bucket = [0] * 6 # A~F까지만 있대

for i in range(len(str)):
    index = ord(str[i]) - 65
    bucket[index] = 1 # 중복 제거해서 알파벳 순서대로 출력이니 +=1 필요없음

answer = ''

for i in range(len(bucket)):
    if bucket[i] == 1:
        answer += chr(i+65)

print(answer)