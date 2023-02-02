#230202
def is_proper(word):
    improper, proper = f'<{word}> is not acceptable.', f'<{word}> is acceptable.'
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    for alp in word:
        if alp in vowel_set:
            break
    else:
        return improper

    vowel = consonant = 0
    length = len(word)

    if length == 1:
        return proper

    if word[0] in vowel_set:
        vowel += 1
    else:
        consonant += 1

    for i in range(1, length):
        alp = word[i]
        if alp == word[i-1] and alp not in {'e', 'o'}:
            return improper

        if alp in vowel_set:
            vowel += 1
            consonant = 0
        else:
            consonant += 1
            vowel = 0

        if vowel == 3 or consonant == 3:
            return improper

    return proper

while True:
    word = input()
    if word == 'end':
        break
    print(is_proper(word))

''