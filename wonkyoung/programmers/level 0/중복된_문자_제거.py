#230114
def solution(my_string):
    answer = ''
    munja = set()
    for alp in my_string:
        if alp not in munja:
            answer += alp
            munja.add(alp)
    return answer