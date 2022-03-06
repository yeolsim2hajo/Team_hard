arr = list(input().split())
cnt = 0
for i in range(len(arr)):
    if ord('0') <= ord(arr[i]) <= ord('9'):
        cnt += 1


if cnt > 0:
    print('숫자{}개발견'.format(cnt))
else:
    print('숫자미발견')