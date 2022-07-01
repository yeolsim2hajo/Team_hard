#16960 스위치와 램프
# N, M = map(int, input().split())
# link = []
# for _ in range(N):
#     link.append(list(map(int,input().split()))[1:])
# numbers = set(range(1,M+1))
# lamp = set()
# possible = 0
# def is_possible(arg=0):
#     global possible
#     if possible:
#         return
#     if arg == N-1:
#         if lamp == numbers:
#             possible = 1
#         return
#     for i in range(N):
#         lamp.update(set(link[i]))
#         is_possible(arg+1)
#         lamp.discard(set(link[i]))
#         print(lamp, numbers)
# is_possible()
# print(possible)
#
# print({1,2,3}.discard(1))
# print({1,2,3}.remove(1))



#1032 명령 프롬프트
N = int(input())
file = [list(map(str,input())) for _ in range(N)]
length = len(file[0])
answer = ''
for i in range(length):
    alp = file[0][i]
    for j in range(1,N):
        if file[j][i] != alp:
            answer += '?'
            break
    else:
        answer += alp
print(answer)
