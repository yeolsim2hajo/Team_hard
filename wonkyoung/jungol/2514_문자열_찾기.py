#221117
input_word = input()
for word in ('KOI', 'IOI'):
    cnt = 0
    for i in range(len(input_word) - 2):
        if input_word[i:i+3] == word:
            cnt += 1
    print(cnt)