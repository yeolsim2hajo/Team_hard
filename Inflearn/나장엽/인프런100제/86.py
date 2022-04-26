point = list(map(int,input().split()))
dish = int(input())
def chobap():
    length = len(point)
    scores = [0] * (length + 1)
    for num in point:
        scores[num] += 1
    cnt = -1
    idx = 0
    for i in range(1,length+1):
        while scores[i]:
            if point[idx]:
                cnt += 1
                if point[idx] == i:
                    if idx == dish-1:
                        return cnt
                    point[idx] = 0
                    scores[i] -= 1
            idx += 1
            if idx >= len(point):
                idx = 0
print(chobap())