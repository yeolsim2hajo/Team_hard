#230205
def solution(id_pw, db):
    answer = ''
    for info in db:
        if info == id_pw:
            return 'login'
        elif info[0] == id_pw[0]:
            answer = 'wrong pw'
    return answer or 'fail'