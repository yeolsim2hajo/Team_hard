arr = [['D','A','T','A','W',''], ['B','B','Q','K','','']]
num = int(input())
if num % 2:
    arr[0].sort()
    for i in range(2):
        print(*arr[i],sep='')
else:
    arr[1].sort()
    for i in range(2):
        print(*arr[i],sep='')
