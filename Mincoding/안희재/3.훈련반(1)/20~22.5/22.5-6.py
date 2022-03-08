# 버블 소트 사용
arr = [input() for _ in range(4)]

for i in range(3):
    for j in range(3-i):
        if len(arr[j]) > len(arr[j+1]):
            arr[j], arr[j+1] = arr[j+1], arr[j]

for i in range(4):
    print(arr[i])