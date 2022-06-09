# 이항계수
# 조합론에서 등장하는 개념으로 주어진 크기의 집합에서 원하는 개수만큼 순서없이 뽑는 조합의 가짓수
# 이항 :  뽑거나, 안 뽑거나
# 성질 1: nCk = n! / (n-k)!k! (단, 0 <= k <= n)
# 성질 2: n개 중에서 k개를 선택하는 것은 선택받지 않은 나머지 n-k를 선택하는 것과 같음
# 성질 3: nCk = (n-1) C (k) + (n-1) C (k-1)

# 팩토리얼을 구하여 공식대로 구현하기



# def factorial(n):
#     ans = 1
#     for i in range(2, n+1):
#         ans *= i
#     return ans

# def bino_coef_factorial(n, k):
#     return factorial(n) // factorial(k) // factorial(n-k)


# 주의점 : 팩토리얼 함수가 0! 이어도 1을 문제없이 반환할 수 있도록 해야 함. 그렇지 않다면 밑의 이항계수 함수가 zerodivisionError
# 오버플로우가 발생할 수 있다. n이 15만 되어도 계산이 1조를 훌쩍 넘는다.


# 동적 계획법 1 : 이항 계수의 성질을 이용하기
# 기억하며 풀기.
# 전체 집합에서 아무것도 고르지 않는 방법은 1가지, 동시에 모두를 선택하는 것도 1가지
# 이항계수를 그 보다 작은 두개의 부분식으로 쪼갤 수 있고, 이 식들은 더 잘게 잘게 쪼개질 수 있다. 쪼개지면서 n과 k가 점차 작아지는데, k가 0이 되는 순간과 n과 k가 같아지는 순간은 무조건 1

# def bino_coef(n, k):
#     if k == 0 or n == k:
#         return 1
#     return bino_coef(n-1, k) + bino_coef(n-1, k-1)

# 부분 문제의 중복으로 함수의 성능이 나쁨.
# 원 문제를 풀기위한 부분문제의 중복으로 인해 시간을 잡아먹는다.
# 성능개선을 위해 이미 구한 부분 문제의 답을 저장해서 또 구해야 할 때에는 바로 답을 내놓고 쓸데없는 계산을 하지 말아야 한다.

def bino_coef(n, k): 
    # n은 0 부터 n 까지, k는 0부터 k까지의 범위를 지닌다. 따라서 총 가능한 이항계수의 가지 수는 (n+1)*(k+1) 
    # cache 초기화
    cache = [[0 for _ in range(k+1)] for _ in range(n+1)]

    # k가 0 이거나, n이 k와 같은 경우 check 
    # 위의 경우 이항계수의 성질에 따라 1이 된다.
    for i in range(n+1):
        cache[i][0] = 1
    for i in range(k+1):
        cache[i][i] = 1

    # 실제 계산  : i개의 아이템 중에서 j개의 아이템을 선택하는 경우의 수는 그보다 작은 두 값의 합.
    for i in range(1, n+1):
        for j in range(1, k+1):
            cache[i][j] = cache[i-1][j] + cache[i-1][j-1]
    print(cache)
    return cache[n][k]

n, k = map(int, input().split())
print(bino_coef(n, k))