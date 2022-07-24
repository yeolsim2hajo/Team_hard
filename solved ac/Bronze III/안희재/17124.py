# 모든 탐색 -> 시간초과
    # => 이진탐색(binary search)
    # 선정렬 필수
    # 유튜브 영상참고(https://www.youtube.com/watch?v=VxLEDVZKinA)
    # 코드 작성방법이 생소했음

def solve():
    n, m = [int(x) for x in input().split()]
    A = [int(x) for x in input().split()]
    B = [int(x) for x in input().split()]
    B.sort() # 선정렬
    s = 0