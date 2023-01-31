#230201
def solution(array):
    length = len(array)
    max_val = max_i = -1
    for i in range(length):
        if array[i] > max_val:
            max_val = array[i]
            max_i = i
    return [max_val, max_i]
'''
테스트 1 〉	통과 (0.00ms, 10.3MB)
테스트 2 〉	통과 (0.00ms, 10.1MB)
'''

def solution(array):
    sorted_arr = sorted(enumerate(array), key=lambda x: x[1])
    return list(sorted_arr[-1])[::-1]
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
'''