arr = [3,5,1,2,4,6,7]

num = list(map(int,input().split()))

print(' '.join(map(str,arr[num[0]:num[1]+1])))