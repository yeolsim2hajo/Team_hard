def abc(frame, page):
    page = page.split()
    time = 0
    result = list()


    if frame == 0:
        time = len(page)*6
        return time

    for i in page:
        if i in result:
            time += 1
        else:
            if len(result) < frame:
                result.append(i)

        time +=  6


    return time


frame = int(input())
page = list(input())

print(abc(frame, page))