def solution(n, k):
    from math import factorial
    answer = []
    order = list(range(1, n+1))
    cnt = factorial(n-1)
    k -= 1
    for i in range(1, n+1):
        if k:
            answer.append(order.pop(k//cnt))
            k %= cnt
            cnt //= (n-i)
        else:
            answer.append(order.pop(0))
    return answer