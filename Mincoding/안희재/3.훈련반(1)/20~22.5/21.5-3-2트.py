word = list(input())
a, b = input().split()

# 흠; 그냥 a,b가 word에서 몇번 인덱스인지 찾은 후에 풀어야 하나;?
# 아 ㄴㄴ 내 처음 풀이와 연계해서 풀면 되네

for i in range(len(word)):
    if word[i] == a:
        if i-1 >= 0:
            word[i-1] = '#'
        if i+1 < len(word):
            word[i+1] = '#'
    elif word[i] == b:
        if i-1 >= 0:
            word[i-1] = '#'
        if i+1 < len(word):
            word[i+1] = '#'

print(''.join(word))
