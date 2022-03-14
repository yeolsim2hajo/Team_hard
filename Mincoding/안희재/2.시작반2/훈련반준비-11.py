arr = ['A','P','P','L','E','T']
word = input().split()

cnt = 0
for i in range(6):
    for j in range(5):
        if arr[i] == word[j]:
            cnt += 1

print(f'{cnt}개 맞추었습니다')

# L E P A T