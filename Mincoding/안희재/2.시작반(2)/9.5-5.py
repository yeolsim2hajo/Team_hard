word = input().split()
arr = [[''] * 3 for _ in range(2)]

idx = 0
for i in range(2):
    for j in range(3):
        arr[i][j] = word[idx]
        idx += 1

def findUpper():
    cnt = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j].isupper() == 1:
                cnt += 1
    print(f'대문자{cnt}개')

def findLower():
    cnt = 0
    for i in range(2):
        for j in range(3):
            if arr[i][j].islower() == 1:
                cnt += 1
    print(f'소문자{cnt}개')

findUpper()
findLower()