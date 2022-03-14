word1 = input()
word2 = input()
a = sorted(word1)
b = sorted(word2)

print(*(a+b),sep='')