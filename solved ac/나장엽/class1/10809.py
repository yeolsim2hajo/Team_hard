S = list(input())
check = [-1]*26
alpha = []
for i in range(97, 123):
    alpha.append(chr(i))

for i in range(len(S)):
    for k in range(len(alpha)):
        if check[k] != -1:
                continue
        if S[i] == alpha[k]:
            check[k] = i

print(*check, sep = ' ')