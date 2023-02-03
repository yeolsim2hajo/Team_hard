#230203
def solution(common):
    dif = common[1] - common[0]
    if dif == common[2] - common[1]:
        return common[-1] + dif
    multiple = common[1] // common[0]
    return common[-1] * multiple