# 논리구조 주목
def sol(frame, page):
    temp = []
    runTime = 0

    if frame == 0:
        runTime = len(page) * 6
        return runTime

    for i in page:
        if i in temp:
            temp.append(temp.pop(0))
            runTime += 1
        else:
            if len(temp) < frame:
                temp.append(i)
            else:
                temp = temp[1:] + [i]
            runTime += 6

    return runTime