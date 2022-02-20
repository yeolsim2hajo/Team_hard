# 이야 이건 DAT로 풀면 딱 좋은 문제네
# 이런 유형 인지해두자!
bucket = [0] * 26

for i in range(3):
    str = list(input())
    for j in range(len(str)):
        index = ord(str[j])-65 
        bucket[index] += 1

for i in bucket:
    if i >= 2:
        print('No')
        break
else:
    print('Perfect')