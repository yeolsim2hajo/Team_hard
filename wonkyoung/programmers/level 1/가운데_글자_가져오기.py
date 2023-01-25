#230125
def solution(s):
    length = len(s)
    half = length//2
    if length % 2:
        return s[half]
    return s[half-1:half+1]