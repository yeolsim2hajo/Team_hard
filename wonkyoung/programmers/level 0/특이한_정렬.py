#230126
def solution(numlist, n):
    length = len(numlist)
    def find_dif(number):
        return (abs(number-n), -number)
    numlist = list(map(find_dif, numlist))
    numlist.sort()
    answer = [-num[1] for num in numlist]
    return answer
'''
테스트 1 〉	통과 (0.03ms, 9.97MB)
테스트 2 〉	통과 (0.05ms, 10MB)
테스트 3 〉	통과 (0.02ms, 10.1MB)
테스트 4 〉	통과 (0.04ms, 10.4MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
'''

def solution(numlist, n):
    numlist.sort(key= lambda num: (abs(num-n), -num))
    return numlist
'''
테스트 1 〉	통과 (0.03ms, 10.1MB)
테스트 2 〉	통과 (0.07ms, 10.1MB)
테스트 3 〉	통과 (0.02ms, 10MB)
테스트 4 〉	통과 (0.03ms, 10.1MB)
테스트 5 〉	통과 (0.01ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
'''

def solution(numlist, n):
    answer = sorted(numlist, key= lambda num: (abs(num-n), -num))
    return answer
'''
테스트 1 〉	통과 (0.02ms, 10MB)
테스트 2 〉	통과 (0.03ms, 10.2MB)
테스트 3 〉	통과 (0.02ms, 10.3MB)
테스트 4 〉	통과 (0.02ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 9.93MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
'''

def solution(numlist, n):
    length = len(numlist)
    dif = list(map(lambda x: abs(x-n), numlist))
    for i in range(length-1):
        for j in range(length-1-i):
            if dif[j] > dif[j+1]:
                dif[j], dif[j+1] = dif[j+1], dif[j]
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
            elif dif[j] == dif[j+1] and numlist[j] < numlist[j+1]:
                numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
    return numlist
'''
테스트 1 〉	통과 (0.48ms, 10.1MB)
테스트 2 〉	통과 (1.28ms, 10.3MB)
테스트 3 〉	통과 (0.49ms, 10.2MB)
테스트 4 〉	통과 (0.52ms, 10.1MB)
테스트 5 〉	통과 (0.02ms, 10.1MB)
테스트 6 〉	통과 (0.02ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.1MB)
'''