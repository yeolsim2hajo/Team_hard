#230219
def solution(bin1, bin2):
    answer = int(bin1, 2) + int(bin2, 2)
    return bin(answer)[2:]
'''
테스트 1 〉	통과 (0.00ms, 10MB)
테스트 2 〉	통과 (0.00ms, 10MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10.2MB)
테스트 5 〉	통과 (0.00ms, 10MB)
테스트 6 〉	통과 (0.00ms, 10.2MB)
테스트 7 〉	통과 (0.00ms, 10MB)
테스트 8 〉	통과 (0.00ms, 10.2MB)
테스트 9 〉	통과 (0.00ms, 10MB)
'''

def solution(bin1, bin2):
    if len(bin1) > len(bin2):
        bin1, bin2 = bin2, bin1
    bin1 = list(map(str, bin1[::-1]))
    bin2 = list(map(str, bin2[::-1]))
    length = len(bin1)
    answer = []
    one = False
    for i in range(length):
        num1, num2 = bin1[i], bin2[i]
        if num1 == num2 == '1':
            if one:
                answer.append('1')
            else:
                answer.append('0')
                one = True
        elif num1 == num2 == '0':
            if one:
                answer.append('1')
                one = False
            else:
                answer.append('0')
        elif one:
            answer.append('0')
        else:
            answer.append('1')
    if one:
        for i in range(length, len(bin2)):
            if bin2[i] == '1':
                answer.append('0')
                one = True
            else:
                if one:
                    answer.append('1')
                else:
                    answer.append('0')

                return ''.join((answer + bin2[i+1:])[::-1])
    else:
        return ''.join((answer + bin2[length:])[::-1])
    if one:
        answer.append('1')
    return ''.join(answer[::-1])
'''
테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.01ms, 10.3MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.03ms, 10.2MB)
테스트 5 〉	통과 (0.01ms, 10.4MB)
테스트 6 〉	통과 (0.01ms, 10.3MB)
테스트 7 〉	통과 (0.01ms, 10.3MB)
테스트 8 〉	통과 (0.01ms, 10.2MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
'''