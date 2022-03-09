arr = input().split()

idx = []
cnt = 0
for i in range(len(arr)):
    if arr[i] == 'A':
        idx.append(f'{i}번')
        cnt += 1

print(f'문자A는 {cnt}개발견')
for i in idx:
    print(i)