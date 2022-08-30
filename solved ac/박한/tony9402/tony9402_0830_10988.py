# 백준 10988 팰린드롬인지 확인하기

word = input()
W = len(word)
rst = 1
for w in range(W//2+1):
    if word[w] != word[W-w-1]:
        rst = 0
        break
print(rst)