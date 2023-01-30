#230129
def solution(spell, dic):
    length = len(spell)
    for word in dic:
        possible = False
        check = [False] * length
        if len(word) == length:
            for alp in dic:
                for i in range(length):
                    if alp == spell[i]:
                        if not check[i]:
                            check[i] = True
                            possible = True
                            break
                        else:
                            break
                else:
                    break
                if not possible:
                    break
        if possible:
            return 1
    return 2