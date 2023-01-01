def check(word, start, end):
    length = (end - start + 1) // 4
    new_word = 'w' * length + 'o' * length + 'l' * length + 'f' * length
    if word[start:end+1] == new_word:
        return True
    return False

def main():
    word = input()
    # 1 split words
    f_index = []
    for i in range(len(word)):
        if word[i] == 'f' and (i == len(word) - 1 or word[i + 1] != 'f'):
            f_index.append(i)
    f_index.append(len(word) - 1)
    prev = 0
    for idx, f_ind in enumerate(f_index):
        # check 4*n each split word
        if (f_ind + 1) % 4:
            print(0)
            return
        # word is right
        if not check(word, prev, f_ind):
            print(0)
            return
        prev = f_ind + 1
    print(1)

if __name__ == '__main__':
    main()