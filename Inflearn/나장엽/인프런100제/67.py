def solution(n): # 59번의 악수가 진행
    people = 0 #사람
    total = 0
    while(True):
        total = people*(people-1)/2 # 민규를 빼고 한 악수의 총 횟수.
        if n<total:
            break
        people+=1
    times = int(people-(total-n)-1)
    return [times,people]
#??????????????????