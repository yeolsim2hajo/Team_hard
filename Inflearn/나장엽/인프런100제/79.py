

def rotate(list,n) :
    # 리스트 얕은 복사
    l = list[:]
    for i in range(n) :
        l.insert(0,l[-1])
        del l[-1]
    return l

def distance(a,b) :
    lst = []
    for i in range(len(a)) :
        lst.append(abs(a[i]-b[i]))
    return lst

n = 2
before = [10,20,25,27,34,35,39]
after = rotate(before,n)
gap = distance(before,after)

idx = gap.index(min(gap))

print("인덱스 : ",idx)
print("값 : " , before[idx],after[idx])