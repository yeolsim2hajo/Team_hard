#61 문자열 압축하기
# munja = input()
# cnt = 1
# new = ''
# for i in range(len(munja)):
#     if i == len(munja)-1 or munja[i] != munja[i+1]: # 단축 평가 활용
#         new += munja[i]
#         new += str(cnt)
#         cnt = 1
#     else:
#         cnt += 1
# print(new)
#

#62 20190923 출력하기
# munja = 'Z\\'
# hard = str(len(munja))
# hard += str(int(False))
# hard += str(int(True))
# for element in munja:
#     hard += str(ord(element))
# hard += str(ord('D') - ord('A'))
# print(hard)

#63 친해지고 싶어
# munjang = input()
# julim = munjang[0]
# for i in range(1,len(munjang)):
#     if munjang[i-1] == ' ':
#         julim += munjang[i]
# print(julim)

# 다른 방법
# munjang = input().split()
# for i in range(len(munjang)):
#     print(munjang[i][0],end='')


#64 이상한 엘레베이터
# N = int(input())
# seven = N%7
# if seven%3:
#     print(-1)
# else:
#     print(N//7 + seven//3)


#65 변형된 리스트
# a = [1,2,3,4]
# b = ['a','b','c','d']
# c = []
# for i in range(4):
#     if i%2:
#         c.append([b[i],a[i]])
#     else:
#         c.append([a[i], b[i]])
# print(c)


#66 블럭쌓기
# top = input().split()
# rule = input()
# for blocks in top:
#     cnt = 0
#     for block in blocks:
#         if block in rule:
#             if block == rule[cnt]:
#                 cnt += 1

