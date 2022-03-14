max = 0
max_str = ''
for i in range(3):
    word = input()
    if max < len(word):
        max = len(word)
        max_str = word

print(max_str)