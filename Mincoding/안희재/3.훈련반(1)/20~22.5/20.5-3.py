word = input()

length = len(word)

word1 = word[0:length//2]
word2 = word[length//2:]

if word1 == word2:
        print('동일한문장')
else:
        print('다른문장')