# 주사위 던지기 게임
# 3개의 주사위
# s1(2 ~ 20), s2, s3개의 면이 있음
# 세개의 주사위를 동시에 던졌을 때 가장 높은 빈도로 나오는 세 주사위의 합을 구하는 것??
# 1 2 3 
# 1 2
# 1 2 3

# 3 -> 1 1 1
# 4 -> 1 1 2, 1 2 1, 2 1 1
# 5 -> 1 1 3, 3 1 1 
# 6 -> 1 2 3, 2 1 3,

s1, s2, s3 = map(int, input().split())
li = [0]*81
for i in range(1, s1+1):
    for j in range(1, s2+1):
        for k in range(1, s3+1):
            li[i+j+k] += 1
print(li.index(max(li)))