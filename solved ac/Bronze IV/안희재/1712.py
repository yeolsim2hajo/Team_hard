# a, b, c = map(int,input().split())

# if b > c:
#     print(-1)
# else:
#     cnt = 0
#     while a >= 0:
#         a -= (c-b)
#         cnt += 1

#     print(cnt)
# zzzzzzzzzzzzzzzzzzzzzzz시간초과로 실패라니.....................
a, b, c = map(int,input().split())

if b >= c:
    print(-1)
else:
    print(a//(c-b)+1)