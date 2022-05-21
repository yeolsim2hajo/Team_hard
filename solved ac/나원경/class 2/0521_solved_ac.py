#11866 요세푸스 문제 0
# N, K = map(int,input().split())
# people = list(range(1,N+1))
# removed = []
# index = 0
# cnt = 1
# while people:
#     if cnt == K:
#         removed.append(people[index])
#         people.pop(index)
#         index -= 1
#         cnt = 0
#     cnt += 1
#     index += 1
#     if index == len(people):
#         index = 0
# print('<',end='')
# print(*removed, sep=', ', end='')
# print('>')


#15829 Hashing
# alphabet = {chr(97+i):i+1 for i in range(26)}
# L = int(input())
# sentence = input()
# total = 0
# for i in range(L):
#     total += alphabet[sentence[i]] * (31 ** i)
# print(total%1234567891)