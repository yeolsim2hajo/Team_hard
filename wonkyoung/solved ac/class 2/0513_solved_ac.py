#2839 설탕 배달
# N = int(input())
# five, three = N // 5, (N % 5) // 3
# if 5*five + 3*three == N:
#     print(five+three)
# else:
#     total = N//3 + 1
#     possible = False
#     while five >= 0:
#         five -= 1
#         three = (N - 5*five)//3
#         if 5*five + 3*three == N and total > five+three:
#             total = five+three
#             possible = True
#     if possible:
#         print(total)
#     else:
#         print(-1)


# 시간 더 걸림 - 왜?
# N = int(input())
# five, three = N // 5, (N % 5) // 3
# if 5*five + 3*three == N:
#     print(five+three)
# else:
#     total = N//3 + 1
#     while five >= 0:
#         five -= 1
#         three = (N - 5*five)//3
#         if 5*five + 3*three == N and total > five+three:
#             print(five+three)
#             break
#     else:
#         print(-1)


#2869 달팽이는 올라가고 싶다
# A, B, V = map(int,input().split())
# # V <= day * (A-B) + A
#
# day = (V-A) // (A-B)
# snail = day * (A-B)
# while True:
#     day += 1
#     snail += A
#     if snail >= V:
#         break
#     snail -= B
# print(day)