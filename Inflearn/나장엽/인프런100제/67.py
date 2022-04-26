def solution(n): # 59번의 악수가 진행
    people = 0 #사람
    total = 0
    while(True):
        total = people*(people-1)/2 # 민규를 빼고 한 악수의 총 횟수.
        if n<total:
            break
        people+=1
    times = int(people-(total-n)-1)
    return [times,people]
#??????????????????


# 원경님 풀이
# n = int(input())
# people = int((2 * n) ** (0.5)) # 민규 제외 사람 추정
# while True:
#     if (people ** 2 + people) // 2 > n:
#         total = (people ** 2 - people) // 2
#         break
#     people += 1
# print([n-total,people+1])

# 한님 풀이
# n = int(input())
# a, b = 0, 0
# for i in range(n):
#     if i*(i-1)//2 < n < i*(i+1)//2:
#         b = i+1
#         a = n - i*(i-1)//2
#         break
# print(a, b)