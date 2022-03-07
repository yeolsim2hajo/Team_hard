a, b = map(int,input().split())

arr = [a+b*i for i in range(5)]

print(' '.join(map(str,arr)))