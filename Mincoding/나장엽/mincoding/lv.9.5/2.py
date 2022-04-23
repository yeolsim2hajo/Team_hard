arr = list(input().split())

str = 'A'
cnt = 0
idx = []
for i in range(len(arr)):
    if arr[i] == str:
        idx.append(i)
        cnt += 1


print(f'문자A는 {cnt}개발견')

for i in range(len(idx)):
    print(f'{idx[i]}번')