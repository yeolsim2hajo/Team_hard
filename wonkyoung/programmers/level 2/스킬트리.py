#230128
def solution(skill, skill_trees):
    answer, length = 0, len(skill)
    skill_order = {skill[i] : i for i in range(length)}
    for candidate in skill_trees:
        index = 0
        for alp in candidate:
            if skill_order.get(alp, -1) != -1:
                if skill_order[alp] != index:
                    break
                else:
                    index += 1
        else:
            answer += 1
    return answer
solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])