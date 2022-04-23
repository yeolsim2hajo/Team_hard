arr = list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] < 5:
        print(f'{i}번은 {arr[i]}점 불합격')
    else:
        print(f'{i}번은 {arr[i]}점 합격')
