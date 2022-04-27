# 컨테이너 운반
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int,input().split()) # 컨테이너, 트럭
#     weight = list(map(int,input().split()))
#     limit = list(map(int,input().split()))
#     weight.sort() # 오름차순 (작 -> 큰)
#     limit.sort() # 오름차순 (작 -> 큰)
#     max_weight = 0
#     while weight and limit:
#         package = weight.pop()
#         truck = limit.pop()
#         if package <= truck:
#             max_weight += package
#         else:
#             limit.append(truck)
#     print(f'#{tc} {max_weight}')

