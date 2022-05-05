#2675 문자열 반복
# T = int(input())
# for _ in range(T):
#     R, C = input().split()
#     R = int(R)
#     new = ''
#     for alp in C:
#         new += alp * R
#     print(new)


#2739 구구단
# N = int(input())
# for i in range(1,10):
#     print('{} * {} = {}'.format(N, i, N*i))

#2741 N 찍기
# N = int(input())
# for i in range(N):
#     print(i+1)

#2742 기찍 N
# N = int(input())
# for i in range(N,0,-1):
#     print(i)

#2884 알람시계
# H, M = map(int,input().split())
# alarm = H * 60 + M - 45 if H or M >= 45 else (H+24) * 60 + M - 45
# H, M = divmod(alarm, 60)
# print(H, M)

#2908 상수
A, B = input().split()
A = A[::-1]
B = B[::-1]
# int로 바꿔주지 않아도 됨
if A > B:
    print(A)
else:
    print(B)