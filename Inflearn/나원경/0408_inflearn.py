#75 이상한 369
# number = int(input())
# number //= 3
# length = len((str(number))) # 자리수
# clap = 0
# for i in range(1,length+1):
#     a,b = divmod(number,10)
#     clap += b*(3**(i-1)) if 1 <= b <= 3 else 3
#     number = a
# print(clap)

#77 가장 긴 공통 부분 문자열
'''
thisisstrings
thisis

thisisstrings
tathisiskkqqaew

thisisstrings
kiothikessiskkqqaew

thisisstring
tkhkiksis
'''
#83


#86 회전 초밥
'''
1 1 3 2 5
3

5 2 3 1 2 5
1
'''
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


#90
#92
#94
#96
