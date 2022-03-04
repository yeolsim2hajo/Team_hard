# 엘리베이터를 타고 내려가자

# 1중 for문으로 아래와 같이 출력하세요

#9 6
#8 5
#7 4
#6 3

# 풀이 1
for i in range(9, 2, -1):
    if i > 5:
        print('{} {}'.format(i, i-3))
# # 풀이 2
# for i in range(9, 5, -1):
#     print('{} {}'.format(i, i-3))