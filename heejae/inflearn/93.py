# q알고리즘같은데 그냥.. 
    # 쨋든, 구현방식과 논리 순서 잘 기억해두기!
def solution(frame, page):
    page = page.split(' ')
    runTime = 0
    temp = []

    if frame == 0:
        runTime = len(page) * 6
        return runTime

    for i in page:
        if i in temp:
            runTime += 1
        else:
            if len(temp) < frame:
                temp.append(i)
            else:
                temp = temp[1:] + [i]
            runTime += 6
    
    return runTime

f = int(input())
page = list(map(str,input()))


print(solution(f, page))