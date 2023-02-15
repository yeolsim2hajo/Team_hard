#230215
def solution(my_string):
    answer = []
    for element in my_string:
        if element.isdigit():
            answer.append(int(element))
    answer.sort()
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.02ms, 10.3MB)
테스트 3 〉	통과 (0.02ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
'''
#
def solution(my_string):
    answer = [int(element) for element in my_string if element.isdigit()]
    answer.sort()
    return answer
'''
테스트 1 〉	통과 (0.04ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
'''

def solution(my_string):
    answer = sorted(int(element) for element in my_string if element.isdigit())
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.5MB)
테스트 2 〉	통과 (0.02ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.4MB)
테스트 4 〉	통과 (0.02ms, 10.4MB)
'''


def solution(my_string):
    my_string = sorted(my_string)
    answer = []
    for element in my_string:
        if element.isdigit():
            answer.append(int(element))
        else:
            return answer
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10.4MB)
테스트 2 〉	통과 (0.02ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.3MB)
'''
def solution(my_string):
    my_string = sorted(my_string)
    answer = []
    try:
        for element in my_string:
            answer.append(int(element))
        return answer
    except Exception:
        return answer
'''
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.03ms, 10.4MB)
테스트 3 〉	통과 (0.03ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.3MB)
'''