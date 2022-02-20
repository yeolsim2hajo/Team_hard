# 와 이것도 DAT로 풀면 딱이겠네 ㄷㄷ;; 흠..흠!!
# count(), dict등등 다양한 방법이 있겠지만
str = list(input())

bucket = [0] * 26

for i in range(len(str)):
    index = ord(str[i])-65
    bucket[index] += 1

for i in range(len(bucket)):
    if bucket[i] >= 1:
        print(f'{chr(i+65)}:{bucket[i]}')