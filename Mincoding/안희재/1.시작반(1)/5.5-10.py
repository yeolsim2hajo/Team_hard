num = int(input())

arr = [num*i for i in range(1,7)]

for i in range(len(arr)):
    print(arr[i], end = ' ')
# join말고, 위 처럼 해도 가능~!
# print(' '.join(map(str,arr)))