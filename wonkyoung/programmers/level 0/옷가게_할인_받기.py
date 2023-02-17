#230217
def solution(price):
    from math import floor
    if price >= int(5e5):
        return floor(price*0.8)
    elif price >= int(3e5):
        return floor(price*0.9)
    elif price >= int(1e5):
        return floor(price*0.95)
    return price
'''
테스트 1 〉	통과 (0.01ms, 10.3MB)
테스트 2 〉	통과 (0.01ms, 10.2MB)
테스트 3 〉	통과 (0.01ms, 10MB)
테스트 4 〉	통과 (0.01ms, 10MB)
테스트 5 〉	통과 (0.01ms, 10MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.01ms, 10MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.1MB)
테스트 12 〉	통과 (0.01ms, 10MB)
테스트 13 〉	통과 (0.01ms, 10.1MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.2MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.1MB)
테스트 19 〉	통과 (0.01ms, 10MB)
테스트 20 〉	통과 (0.01ms, 10.1MB)
'''
def solution(price):
    from math import floor
    ref = int(1e5)
    if price >= 5*ref:
        return floor(price*0.8)
    elif price >= 3*ref:
        return floor(price*0.9)
    elif price >= ref:
        return floor(price*0.95)
    return price
'''
테스트 1 〉	통과 (0.01ms, 10MB)
테스트 2 〉	통과 (0.01ms, 10.1MB)
테스트 3 〉	통과 (0.01ms, 10.3MB)
테스트 4 〉	통과 (0.01ms, 10.3MB)
테스트 5 〉	통과 (0.01ms, 10.2MB)
테스트 6 〉	통과 (0.01ms, 10.1MB)
테스트 7 〉	통과 (0.01ms, 10.2MB)
테스트 8 〉	통과 (0.00ms, 10.1MB)
테스트 9 〉	통과 (0.01ms, 10.1MB)
테스트 10 〉	통과 (0.01ms, 10.2MB)
테스트 11 〉	통과 (0.01ms, 10.3MB)
테스트 12 〉	통과 (0.01ms, 10.2MB)
테스트 13 〉	통과 (0.01ms, 10.3MB)
테스트 14 〉	통과 (0.01ms, 10.1MB)
테스트 15 〉	통과 (0.01ms, 10.1MB)
테스트 16 〉	통과 (0.01ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.1MB)
테스트 18 〉	통과 (0.01ms, 10.3MB)
테스트 19 〉	통과 (0.01ms, 10.2MB)
테스트 20 〉	통과 (0.01ms, 10.2MB)
'''
def solution(price):
    ref = int(1e5)
    if price >= 5*ref:
        return int(price*0.8)
    elif price >= 3*ref:
        return int(price*0.9)
    elif price >= ref:
        return int(price*0.95)
    return price
'''
테스트 1 〉	통과 (0.00ms, 10.2MB)
테스트 2 〉	통과 (0.00ms, 10.2MB)
테스트 3 〉	통과 (0.00ms, 10.2MB)
테스트 4 〉	통과 (0.00ms, 10MB)
테스트 5 〉	통과 (0.00ms, 10.2MB)
테스트 6 〉	통과 (0.00ms, 10.1MB)
테스트 7 〉	통과 (0.00ms, 10.1MB)
테스트 8 〉	통과 (0.00ms, 10.3MB)
테스트 9 〉	통과 (0.00ms, 10.1MB)
테스트 10 〉	통과 (0.00ms, 10.1MB)
테스트 11 〉	통과 (0.00ms, 10.1MB)
테스트 12 〉	통과 (0.00ms, 10.3MB)
테스트 13 〉	통과 (0.00ms, 10MB)
테스트 14 〉	통과 (0.00ms, 10.3MB)
테스트 15 〉	통과 (0.00ms, 10.1MB)
테스트 16 〉	통과 (0.00ms, 10.1MB)
테스트 17 〉	통과 (0.00ms, 10.2MB)
테스트 18 〉	통과 (0.00ms, 10.2MB)
테스트 19 〉	통과 (0.00ms, 10.2MB)
테스트 20 〉	통과 (0.00ms, 10.1MB)
'''