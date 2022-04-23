word = input()

def check(str):
    if word.count('(') != word.count(')'):
        return False

    tmp = []
    for ele in word:
        if ele == '(':
            tmp.append(ele)
        else: # ')'면
            if len(tmp) == 0:
                return False
            else:
                tmp.pop()

    return True

print(check(word))

