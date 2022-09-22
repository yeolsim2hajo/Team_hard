#220922
def find_remain():
    from math import comb
    N, K = map(int, input().split())
    return comb(N, K)%10007
print(find_remain())
