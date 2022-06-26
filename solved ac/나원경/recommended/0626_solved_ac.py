#16439 치킨치킨치킨
# N, M = map(int,input().split())
# preference = list(zip(*[list(map(int,input().split())) for _ in range(N)]))
# for i in range(M):
#     for j in range(i+1, M):
#         for k in range(j+1, M):
#             lst = [preference[i], preference[j], preference[k]]



#13699 점화식
N = int(input())
result = [1]
def find_answer(arg=0, value=0):
    if arg == i:
        result.append(value)
        return
    find_answer(arg+1, value+result[arg]*result[i-arg-1])


for i in range(1,N+1):
    find_answer()
print(result[N])