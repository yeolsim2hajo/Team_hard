def solution(point, dish):
    dish -=1
    answer = 0
    s = sorted(point)
    while True:
        p = point.pop(0)
        if s[0]==p:
            if dish == 0:
                break
            dish-=1
            s.pop(0)
        else:
            point.append(p)
            dish = len(point)-1 if dish==0 else dish-1
        answer+=1
    return answer
