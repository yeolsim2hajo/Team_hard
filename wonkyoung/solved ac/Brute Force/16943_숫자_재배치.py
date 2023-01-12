#221013
A, B = input().split()
A = sorted(map(str, A), reverse=True)
int_A = list(map(int, A))
answer = -1
ref = int(B)
length = len(A)

def dfs(level, number):
    global answer
    if answer != -1:
        return
    if level == length:
        number = int(number)
        if number < ref:
            answer = max(answer, number)
        return
    for j in range(length):
        if visited[j] == 0:
            visited[j] = 1
            dfs(level+1, number + A[j])
            visited[j] = 0

visited = [0] * length
for i in range(length):
    if int_A[i]:
        if A[i] <= B[0]:
            visited[i] = 1
            dfs(1, A[i])
            if answer != -1:
                break
            visited = [0] * length
    else:
        break

print(answer)