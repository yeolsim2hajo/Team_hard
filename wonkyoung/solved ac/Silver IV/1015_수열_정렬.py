#220928
N = int(input())
A = list(map(int, input().split()))
new_list = list(enumerate(A, start=0))
new_list.sort(key=lambda x:x[1], reverse=True)
print(new_list)
P = [-1] * N
for i in range(N):
    P[new_list[i][0]] = i
print(P)
