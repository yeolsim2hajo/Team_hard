arr= [['G','K','G']]
arr2 = input().split()

arr.append(arr2)

bucket = [0] * 27

# ord('A') = 65
for i in range(2):
    for j in range(3):
        index = ord(arr[i][j])-65 # 'A'는 0번 인덱스에 닮김
        bucket[index] += 1

answer = ''
for i in range(len(bucket)):
    if bucket[i] >= 3:
        answer = '있음'
        break
    else:
        answer = '없음'

print(answer)