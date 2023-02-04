#230204
def solution(quiz):
    answer = []
    for equation in quiz:
        x, operator, y, equal, z = equation.split(' ')
        x, y, z = map(int, [x, y, z])
        x += -y if operator == '-' else y
        if x == z:
            answer.append('O')
        else:
            answer.append('X')
    return answer