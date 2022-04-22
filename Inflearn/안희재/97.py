# 람다 사용법 -> map함수 안에서도 사용 가능!
def sol(n,l):
    answer = 0
    man = [0]*n
    while sum(l)!=0:
        for j in range(len(man)):
            if man[j] == 0 and l:
                man[j]+=l.pop(0)
        man = list(map(lambda x : x-1,man))
        answer+=1
    answer+=max(man)
    return answer

