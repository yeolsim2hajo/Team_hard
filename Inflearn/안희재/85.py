# 인프런의 방식도 익숙해져야 할듯
# 함수명 solution, rule도 괜찮은듯
def solution(n):
    ans='1'
    if n == 1:
        return ans
    for i in range(1,n):
        ans = rule(ans)
    return ans

def rule(n):
    num = max([int(i) for i in n])
    d = [str(i)+str(str(n).count(str(i))) for i in range(1,num+1)]
    return ''.join(d) # 아예 join의 결과를 리턴할 수도 있음!