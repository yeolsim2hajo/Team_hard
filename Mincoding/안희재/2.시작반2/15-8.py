max = 0
result = ''
for i in range(5):
    word = input()
    if len(word) > max:
        max = len(word)
        result = word

print(result)
