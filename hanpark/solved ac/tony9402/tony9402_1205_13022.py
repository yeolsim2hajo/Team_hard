# 백준 13022 늑대와 올바른 단어

import sys
input = sys.stdin.readline

def check(w, s, e):
    l = (e - s + 1) // 4
    nw = 'w' * l + 'o' * l + 'l' * l + 'f' * l
    if w[s:e+1] == nw:
        return True
    return False

def main():
    word = input()
    f_index = []
    for i in range(len(word)):
        if word[i] == 'f' and (i == len(word) - 1 or word[i + 1] != 'f'):
            f_index.append(i)
    f_index.append(len(word) - 1)
    prev = 0
    for idx, f_ind in enumerate(f_index):
        if (f_ind + 1) % 4:
            print(0)
            return
        if not check(word, prev, f_ind):
            print(0)
            return
        prev = f_ind + 1
    print(1)

if __name__ == '__main__':
    main()