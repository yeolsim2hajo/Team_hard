S = input()
word = []

for i in range(len(S) - 2):
    for j in range(i + 1, len(S) - 1):
        for k in range(j + 1, len(S)):
            temp = S[:j][::-1] + S[j:k][::-1] + S[k:][::-1]
            word.append(temp)


print(min(word))