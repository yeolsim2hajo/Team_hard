arr = list(map(int, input().split()))    
cnt = 0
for i in range(len(arr)):
    if 3<=arr[i]<=7:
        cnt += 1
print(cnt)