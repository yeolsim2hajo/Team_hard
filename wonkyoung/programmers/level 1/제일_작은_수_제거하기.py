#230128
def solution(arr):
    length = len(arr)
    if length == 1:
        return [-1]
    min_num = min(arr)
    arr.remove(min_num)
    return arr
'''
테스트 1 〉	통과 (0.89ms, 15.7MB)
테스트 2 〉	통과 (0.01ms, 9.95MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.2MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.02ms, 10.4MB)
테스트 16 〉	통과 (0.03ms, 10.3MB)
'''

def solution(arr):
    length = len(arr)
    if length == 1:
        return [-1]
    min_num, index = arr[0], 0
    for i in range(1, length):
        if arr[i] < min_num:
            min_num = arr[i]
            index = i
    return arr[:index] + arr[index+1:]

'''
테스트 1 〉	통과 (3.07ms, 16MB)
테스트 2 〉	통과 (0.04ms, 10.1MB)
테스트 3 〉	통과 (0.08ms, 10.4MB)
테스트 4 〉	통과 (0.01ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.07ms, 10.2MB)
테스트 7 〉	통과 (0.08ms, 10.4MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.2MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10MB)
테스트 12 〉	통과 (0.01ms, 10.1MB)
테스트 13 〉	통과 (0.01ms, 10.2MB)
테스트 14 〉	통과 (0.07ms, 10.4MB)
테스트 15 〉	통과 (0.03ms, 10MB)
테스트 16 〉	통과 (0.04ms, 10.4MB)
'''