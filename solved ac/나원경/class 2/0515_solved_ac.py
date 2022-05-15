#7568 덩치
# N = int(input())
# info = [list(map(int,input().split())) for _ in  range(N)]
# conf = lambda x, y: x < y
# rating = []
# for people1 in info:
#     cnt = 1
#     for people2 in info:
#         if people1 != people2:
#             weight, height = map(conf, people1, people2)
#             if weight == height == True:
#                 cnt += 1
#     rating.append(cnt)
# print(*rating)


#9012 괄호
# parenthesis = {'(':0, ')':'('}
# T = int(input())
# for _ in range(T):
#     data = input()
#     parenthesis['('] = 0
#     for char in data:
#         if parenthesis['('] < 0:
#             break
#         value = parenthesis[char]
#         if type(value) == int:
#             parenthesis[char] += 1
#         else:
#             parenthesis[value] -= 1
#     if parenthesis['(']:
#         print('NO')
#     else:
#         print('YES')


#10250 ACM 호텔
# T = int(input())
# calc = lambda n,f: (str(n+1) if n+1 >= 10 else '0'+str(n+1), str(f+1))
# for _ in range(T):
#     H, W, N = map(int,input().split())
#     number, floor = divmod(N-1, H)
#     number, floor = calc(number, floor)
#     print(floor+number)