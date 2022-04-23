arr = list(map(int,input().split()))

for i in range(len(arr)):
    if arr[i] >= 70:
        print(f'{i+1}번사람은{arr[i]}점PASS')
    elif arr[i] >= 50:
        print(f'{i+1}번사람은{arr[i]}점RETEST')
    else:
        print(f'{i+1}번사람은{arr[i]}점FAIL')