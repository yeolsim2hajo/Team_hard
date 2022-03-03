arr = input().split()

cnt = 0
for i in arr:
    if ord(i) <= 57:
        cnt += 1

if cnt == 0:
    print('숫자미발견')
else:
    print(f'숫자{cnt}개발견')