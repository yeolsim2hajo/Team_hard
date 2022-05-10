#2609 최대공약수와 최소공배수
# A, B = map(int,sorted(input().split()))
# for i in range(B,0,-1):
#     if A % i == B % i == 0:
#         break
# print(i)
# print(A*B//i)

#2751 수 정렬하기 2
# N = int(input())
# numbers = [0]
# for i in range(1,N+1):
#     numbers.append(int(input()))
#     idx = i
#     while idx > 1:
#         parent = idx//2
#         if numbers[parent] < numbers[idx]:
#             break
#         numbers[parent], numbers[idx] = numbers[idx], numbers[parent]
#         idx = parent
# for i in range(N):
#     numbers[1], numbers[-1] = numbers[-1], numbers[1]
#     print(numbers.pop())
#     idx = 1
#     while idx < len(numbers)//2:
#         child = idx*2
#         if child+1 < len(numbers) and numbers[child] > numbers[child+1]:
#             child += 1
#         if numbers[child] > numbers[idx]:
#             break
#         numbers[child], numbers[idx] = numbers[idx], numbers[child]
#         idx = child
