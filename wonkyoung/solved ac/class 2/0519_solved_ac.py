#10989 수 정렬하기 3
# N = int(input())
# numbers = [int(input()) for _ in range(N)]
# numbers.sort()
# print(*numbers,sep='\n')

#11050 이항 계수 1
N, M = map(int,input().split())
son = mom = 1
for i in range(M):
    son *= (N-i)
    mom *= i+1
print(son//mom)