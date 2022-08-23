#11726 2xn 타일링
# n = int(input())
# if n == 1:
#     print(1)
# else:
#     case = [1,2]
#     while n > len(case):
#         case.append(case[-1]+case[-2])
#     print(case[-1]%10007)

# 2개로 고정
# n = int(input())
# if n <= 2:
#     print(n)
# else:
#     case = [1,2]
#     for _ in range(n-2):
#         case.append(case[0]+case[1])
#         case.pop(0)
#     print(case[-1]%10007)


#deque 이용
# n = int(input())
# if n <= 2:
#     print(n)
# else:
#     from collections import deque
#     case = deque([1,2])
#     for _ in range(n-2):
#         case.append(case[0]+case[1])
#         case.popleft()
#     print(case[-1]%10007)


# 변수 두 개 이용
# n = int(input())
# if n <= 2:
#     print(n)
# else:
#     ppre, pre = 1, 2
#     for _ in range(n-2):
#         ppre, pre = pre, ppre+pre
#     print(pre%10007)