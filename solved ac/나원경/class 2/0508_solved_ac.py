#1966 프린터 큐
# T = int(input())
# for _ in range(T):
#     N, M = map(int,input().split())
#     document = list(map(int,input().split()))
#     for i in range(N):
#         document[i] = (document[i],i)
#     cnt = 1
#     for _ in range(N):
#         reference = document.pop(0)
#         for i in range(len(document)):
#             if document[i][0] > reference[0]:
#                 document.append(reference)
#                 break
#         else:
#             if reference[1] != M:
#                 cnt += 1
#             else:
#                 print(cnt)
#                 break


#1978 소수 찾기
# N = int(input())
# numbers = list(map(int,input().split()))
# cnt = 0
# for number in numbers:
#     if number in {2,3}:
#        cnt += 1
#     elif number%2 and number > 3:
#         for i in range(3,number//2,2):
#             if number%i == 0:
#                 break
#         else:
#             cnt += 1
# print(cnt)