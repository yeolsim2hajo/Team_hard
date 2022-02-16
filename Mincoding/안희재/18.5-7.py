vect = ['M','I','N','C','O','D','I','N','G']
n = int(input())
str_lst = input().split()

bucket = [0] * 26

for i in range(len(vect)):
    index = ord(vect[i])-65 # 'A'는 0번 인덱스
    bucket[index] = 1

answer = ''
for i in range(len(str_lst)):
    if bucket[ord(str_lst[i])-65] == 1:
        answer += 'O'
    else:
        answer += 'X'

print(answer)