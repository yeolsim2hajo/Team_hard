#230104
def solution(A, B):
    length = len(A)
    for i in range(length, -1, -1):
        result = A[i:] + A[:i]
        if result == B:
            return length - i
    return -1