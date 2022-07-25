# 정수 배열 A 와 B가 있다. A는 총 n개의 서로 다른 양의 정수를 포함하고 B는 총 m개의 서로 다른 양의 정수를 포함한다.

# A, B를 이용해서 길이가 n인 새로운 배열 C를 만들어보자.

# C[i] 는 배열 B에 있는 값 중 A[i] 에 가장 가까운 값 (절대값 차이가 가장 작은 값)으로 정의 된다. 
# 만약 이 조건을 만족하는 값들이 여럿 있는 경우, 그 중 가장 크기가 작은 값으로 정의 된다. / 절대값 차이
# 예를 들어 A = [20, 5, 14, 9] 그리고 B = [16, 8, 12] 라고 해보자.

# C[1] = 16 이다 - 왜냐하면 B[1] = 16이 A[1] = 20에 가장 가깝기 때문이다.
# C[2] = 8 이다 - 왜냐하면 B[2] = 8이 A[2] = 5에 가장 가깝기 때문이다.
# C[3] = 12 이다 - 왜냐하면 B[1] = 16 와 B[3] = 12 모두 A[3] = 14에 가장 가깝지만, B[3]의 값이 더 작기 때문이다.
# C[4] = 8이다.
# 이 예제의 경우 C = [16, 8, 12, 8]으로 정의된다.

# 두 배열 A와 B가 주어졌을 때, 새로운 배열 C를 계산하여 배열 C에 포함된 값들의 합을 구하는 프로그램을 작성하시오


# 어디와 가까운지 찾으면 됨 -> 이분탐색

def find(arr):
    now = arr[2]
    result = 2
    if arr[1] <= now:
        now = arr[1]
        result = 1
    if arr[0] <= now:
        now = arr[0]
        result = 0

    return result


def binary_search(target, B, start, end):
    gap = end - start
    # 종료 조건
    if gap <= 1: # start가 답.
        return start
    
    mid = (start + end) // 2
    if target < B[mid]: 
        return binary_search(target, B, start, mid)
    else: # target >= B[mid]
        return binary_search(target, B, mid, end)


t = int(input())
for _ in range (t):
    n, m = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    B.sort()
    Sum = 0

    for i in A: # A의 요소에 대해서, 
        temp = binary_search(i, B, 0, m) # 
        arr = []
        arr.append(abs(B[temp-1] - i))
        arr.append(abs(B[temp] - i))
        arr.append(abs(B[(temp+1) % m] - i)) # 범위가 넘지 않게 % 연산자 사용
        index = find(arr)
        Sum += B[temp + index - 1]
    print(Sum)


    



from os import startfile
import sys
from tkinter import LEFT
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())))

    C = [10**9] * N
    for i in range(N):
        start, end = 0, M-1
        while start<=end:
            mid = (start+end) //2
            if A[i] > B[mid]:
                tmp = C[i]
                if abs(C[i]-A[i]) > abs(A[i]-B[mid]):
                    C[i] = B[mid]
                elif abs(C[i]-A[i]) == abs(A[i]-B[mid]):
                    C[i] = min(C[i], B[mid])

                start = mid+1
            elif A[i] == B[mid]:
                C[i] = B[mid]
                break
            else:
                tmp = C[i]
                if abs(C[i] - A[i]) > abs(A[i] - B[mid]):
                    C[i] = B[mid]
                elif abs(C[i] - A[i]) == abs(A[i] - B[mid]):
                    C[i] = min(C[i], B[mid])
                end = mid-1
    print(sum(C))



t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = sorted(B)

    C = []
    for i in A:
        start = 0
        end = m-1
        while True:
            if start > end:
                if start < m  and abs(B[start] - i) < abs(B[end] - i):
                    num = B[start]
                elif end >= 0:
                    num = B[end]
                break
            mid = (start + end ) // 2

            if B[mid] > i:
                end = mid-1
            elif B[mid] < i:
                start = mid+1
            else:
                num = B[mid]
                break
        C.append(num)
    print(sum(C))