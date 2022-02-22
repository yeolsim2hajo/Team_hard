word = input()

# word = abcd면,
# 3:
# 2:
# 1:
# 0:
for i in range(len(word)-1,-1,-1):
        print(word[i:])