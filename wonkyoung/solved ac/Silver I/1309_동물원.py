#221221
N = int(input())
if N == 1:
    answer = 3
else:
    answer = 2*N + (N-1)*N*(2*N-1)//3 + 1
print(answer % 9901)