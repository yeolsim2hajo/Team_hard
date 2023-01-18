#230118
def solution(array, height):
    answer = 0
    for other_height in array:
        if other_height > height:
            answer += 1
    return answer