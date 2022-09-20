def solution(n):
    people = 0
    total = 0
    while 1:
        total = people*(people-1)//2
        if n<total:
            break
        people+=1
    times = n-(people-1)*(people-2)//2
    return [times,people]

n = int(input())
print(solution(n))