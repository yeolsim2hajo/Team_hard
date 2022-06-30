#1436 영화감독 숌
# N = int(input())
# series = '666'
# num_list = []
# if N == 1:
#     print(series)
# else:
#     N -= 1
#     while 1:
#         num_list.append(str(N)+series,series+str(N))


#1654 랜선 자르기
# def cutting():
#     K, N = map(int,input().split())
#     lines =[int(input()) for _ in range(K)]
#     lines.sort(reverse=True)
#     max_length = sum(lines) // N
#     while True:
#         cnt = 0
#         for i in range(K):
#             if cnt >= N:
#                 print(max_length)
#                 return
#             elif lines[i] >= max_length:
#                 cnt += lines[i]//max_length
#             else:
#                 break
#         if cnt >= N:
#             print(max_length)
#             return
#         max_length -= 1
# cutting()


#1874 스택 수열
# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# def possible():
#     calculator = []
#     stack = []
#     top = -1
#     number = 1
#     for i in range(N):
#         while True:
#             stack.append(number)
#             calculator.append('+')
#             top += 1
#             if numbers[i] == number:
#                 calculator.extend(['+','-'])
#                 number = stack[top]
#                 break
#             elif numbers[i] < number:
#                 print('NO')
#                 return
#             else:
#
#
# possible()


#1920 수 찾기
# N = int(input())
# n_list = set(input().split())
# M = int(input())
# m_list = input().split()
# for i in range(M):
#     if m_list[i] in n_list:
#         print(1)
#     else:
#         print(0)


#1929 소수 구하기
M, N = map(int,input().split())
prime = set(range(2,N+1))
for i in range(2,N+1):
    if i in prime:
        for j in range(2*i,N+1,i):
            try:
                prime.remove(j)
            except:
                continue
        if i < M:
            prime.remove(i)
prime = sorted(prime)
for number in prime:
    print(number)


# 시간 더 적게 걸림
M, N = map(int,input().split())
prime = set(range(2,N+1))
for i in range(2,N+1):
    if i in prime:
        for j in range(2*i,N+1,i):
            if j in prime:
                prime.remove(j)
        if i < M:
            prime.remove(i)
prime = sorted(prime) # 이거 안 쓰면 시간 더 오래 걸림 -  왜?
for number in prime:
    print(number)


# 가장 빠름 - 메모리도 덜 차지
M, N = map(int,input().split())
prime = [True for _ in range(N+1)]
for i in range(2,N+1):
    if prime[i]:
        for j in range(2*i,N+1,i):
            if prime[j]:
                prime[j] = False
        if i >= M:
            print(i)