arr = list(map(int, input().split()))
count = 0
sortList = sorted(arr)

for i in range(len(sortList)-1) :
    if 1 == abs(sortList[i]-sortList[i+1]) :
        count+=1
        continue
    else :
        count = 0
        print('NO')
        break


if count > 0 :
    print('YES')