#220920
def solution(n):
    word = '수박'
    answer = word*(n//2) + word[0]*(n%2)
    return answer
