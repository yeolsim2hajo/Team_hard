#230102
def solution(ingredient):
    answer = index = 0
    length = len(ingredient)
    burger = [1, 2, 3, 1]
    one = []
    while index < length:
        if ingredient[index] == 1:
            if ingredient[index:index + 4] == burger:
                for _ in range(4):
                    ingredient.pop(index)
                if one:
                    index = one.pop()
                length -= 4
                answer += 1
                continue
            else:
                one.append(index)
        index += 1

    return answer