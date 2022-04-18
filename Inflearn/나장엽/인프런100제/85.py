def func(ex) :
    maxNum = max([int(i) for i in str(ex)])
    countNum = [ str(i)+str(str(ex).count(str(i))) for i in range(1,maxNum+1) ]
    return ''.join(countNum)

def soultion(N):
    num = 1
    if N == 1 :
        return num
    else :
        for i in range(N-1) :
            num = func(num)
    return num
N = 6
print(soultion(N))