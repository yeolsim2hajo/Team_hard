word = input()
print(len(word))

cnt = 0
for i in range(len(word)):
    if word[i] == word[-1]:
        cnt += 1

print(cnt)