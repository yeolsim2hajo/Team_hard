# 팩토리얼 0의 개수
# N = int(input())
# result = 1
# for i in range(1,N+1):
#     result *= i
# result = str(result)
# cnt = 0
# for number in result[::-1]:
#     if number != '0':
#         break
#     cnt += 1
# print(cnt)

# 시간 더 나옴
# N = int(input())
# cnt = 0
# two = five = 0
# def mod_zero(n):
#     global number, cnt
#     while number%n == 0:
#         cnt += 1
#         number //= n
# for i in range(1,N+1):
#     number = i
#     while number % 10 == 0:
#         cnt += 1
#         number //= 10
#     while number % 2 == 0:
#         two += 1
#         number //= 2
#     while number % 5 == 0:
#         five += 1
#         number //= 5
#
# print(cnt+min(two,five))


#1697 숨바꼭질 - bfs
# N, K = map(int, input().split())
# min_time = abs(N-K)
# def find_time(position):
#     global min_time
#     visited = [False] * 100001
#     visited[position] = True
#     q = [(position,0)]
#     while q:
#         now, time = q.pop(0)
#         if now == K:
#             min_time = time
#             return
#         if now < K and now <= 50000 and visited[now*2] is False:
#             visited[now * 2] = True
#             q.append((now*2,time+1))
#         if now > 0 and visited[now-1] is False:
#             visited[now - 1] = True
#             q.append((now-1,time+1))
#         if now < 100000 and visited[now+1] is False:
#             visited[now + 1] = True
#             q.append((now+1,time+1))
#
# find_time(N)
# print(min_time)

# dfs - 가지치기 - recursion error
# N, K = map(int, input().split())
# min_time = abs(N - K)
# visited = [False] * 100001
#
# def find_time(now, time=0):
#     global min_time
#     if time >= min_time:
#         return
#     if now == K:
#         min_time = time
#         return
#     if now < K and now <= 50000 and visited[now*2] is False:
#         visited[now * 2] = True
#         find_time(now * 2, time + 1)
#     if now > 0 and visited[now - 1] is False:
#         visited[now - 1] = True
#         find_time(now - 1, time + 1)
#     if now < 100000 and visited[now + 1] is False:
#         visited[now + 1] = True
#         find_time(now + 1, time + 1)
#
# find_time(N)
# print(min_time)


# visited - set - 메모리 더 차지
# N, K = map(int, input().split())
# min_time = abs(N-K)
# def find_time(position):
#     global min_time
#     visited = {position}
#     q = [(position,0)]
#     while q:
#         now, time = q.pop(0)
#         if now == K:
#             min_time = time
#             return
#         if now < K and now <= 50000 and now*2 not in visited:
#             visited.add(now*2)
#             q.append((now*2,time+1))
#         if now > 0 and now-1 not in visited:
#             visited.add(now-1)
#             q.append((now-1,time+1))
#         if now < 100000 and now+1 not in visited:
#             visited.add(now+1)
#             q.append((now+1,time+1))
#
# find_time(N)
# print(min_time)

#1764 듣보잡
# import sys
# N,M = map(int, input().split())
# new_input = sys.stdin.readline
# people_one = set()
# people_two = set()
# for _ in range(N):
#     people_one.add(new_input().rstrip())
# for _ in range(M):
#     people_two.add(new_input().rstrip())
# inter = sorted(people_one & people_two)
#
# print(len(inter))
# for name in inter:
#     print(name)


# inter 없앰
# import sys
# N,M = map(int, input().split())
# new_input = sys.stdin.readline
# people_one = set()
# people_two = set()
# for _ in range(N):
#     people_one.add(new_input().rstrip())
# for _ in range(M):
#     person = new_input().rstrip()
#     if person in people_one:
#         people_two.add(person)
# people_two = sorted(people_two)
#
# print(len(people_two),*people_two,sep='\n')