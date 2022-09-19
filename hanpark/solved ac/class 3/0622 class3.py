# 백준 class 3++ 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())
arr = {}
lst = [input() for _ in range(n)]
ans = [input() for _ in range(m)]

for i in range(n):
    arr[lst[i]] = i+1

arr1 = {v:k for k,v in arr.items()}

for i in range(m):
    if ord('0') <= ord(ans[i][0]) <= ord('9'):
        print(arr1[int(ans[i])])
    else:
        print(arr[ans[i]])
