
leveltable = [[10, 20],[30 ,60],[100, 150],[200, 300]]

cal = list(map(int, input().split()))

#  level 
def level(cal):
    result = []
    for i in range(len(cal)):
        if 10 <= cal[i] <=20:
            result.append(0)
        elif 30 <= cal[i] <=60:
            result.append(1)
        elif 100 <= cal[i] <=150:
            result.append(2)
        elif 200 <= cal[i] <=300:
            result.append(3)
    return result



counting = level(cal)
cnt = [0]*4

for i in range(len(counting)):
    if counting[i] == 0:
        cnt[0] += 1
    elif counting[i] == 1:
        cnt[1] += 1
    elif counting[i] == 2:
        cnt[2] += 1
    elif counting[i] == 3:
        cnt[3] += 1

for k in range(4):
    print("lev{0}:{1}".format(k,cnt[k]))