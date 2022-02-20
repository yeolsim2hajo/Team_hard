arr = list(map(int,input().split()))

bucket = [0] * 10

for i in range(len(arr)):
    index = arr[i]
    bucket[index] += 1

for i in range(len(bucket)):
    if bucket[i] >= 2:
        print('도플갱어 발견')
        break
else:
    print('미발견')
