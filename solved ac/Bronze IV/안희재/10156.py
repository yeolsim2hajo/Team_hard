num = list(map(int, input().split()))

if num[0]*num[1] > num[2]:
    print(num[0]*num[1]-num[2])
else:
    print(0)