#2775 부녀회장이 될테야
# 재귀 이용 -  틀림
# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     def downstair(floor, number):
#         if floor == 1:
#             return n*(n+1)//2
#         total = 0
#         for i in range(1,number+1):
#             total += downstair(floor-1, i)
#         return total
#     print(downstair(k,n))


# T = int(input())
# apartment = [[0]*15 for _ in range(15)]
# apartment[0] = list(range(0,15))
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     for i in range(1,k+1):
#         for j in range(1,n+1):
#             apartment[i][j] = sum(apartment[i-1][:j+1])
#     print(apartment[i][j])