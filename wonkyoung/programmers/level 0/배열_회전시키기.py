#230217
def solution(numbers, direction):
    if direction == 'left':
        number = numbers.pop(0)
        numbers.append(number)
    else:
        number = numbers.pop()
        numbers.insert(0, number)
    return numbers