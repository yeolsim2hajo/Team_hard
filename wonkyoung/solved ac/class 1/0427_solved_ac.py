#1152 단어의 개수 - 다시
# words = input().strip()
# print(words.count(' ')+1)


#1157 단어 공부
# words = input().upper()
# check = {}
# for alp in words:
#     if check.get(alp):
#         check[alp] += 1
#     else:
#         check[alp] = 1
# max_num = 0
# max_alp = ''
# more_two = False
# for key in check.keys():
#     if check[key] > max_num:
#         max_num = check[key]
#         max_alp = key
#         more_two = False
#     elif check[key] == max_num:
#         more_two = True
# if more_two:
#     print('?')
# else:
#     print(max_alp)


#1546 평균
# N = int(input())
# numbers = list(map(int,input().split()))
# total = max_score = 0
# for number in numbers:
#     total += number
#     if max_score < number:
#         max_score = number
# print(total/N * (100/max_score))


#2438 별 찍기 - 1
# N = int(input())
# for i in range(N):
#     print('*'*(i+1))


#2439 별 찍기 - 2
# N = int(input())
# for i in range(1,N+1):
#     print(' '*(N-i)+'*'*i)


#2562 최댓값
max_val = 0
for i in range(9):
    number = int(input())
    if max_val < number:
        max_val = number
        cnt = i+1
print(max_val)
print(cnt)

