word1 = input()
word2 = input()
a = len(word1)

result = '거울문장'
for i in range(a):
    if word1[i] !=  word2[a-1-i]:
        result = '거울문장아님'
        print(result)
        break
else:
    print(result)