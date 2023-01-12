#230113
def solution(numbers):
    answer = set()
    length = len(numbers)
    for i in range(length):
        for j in range(length):
            if i != j:
                answer.add(numbers[i]+numbers[j])
    answer = sorted(answer)
    return answer