#230202
def solution(n, works):
    answer = 0
    length = len(works)
    works.sort()
    min_val = works[0]
    quot, remain = divmod(n, length)
    minus = min_val if quot >= min_val else quot
    if quot:
        works = list(map(lambda target: target - minus, works))
        remain += (quot-minus) * length
    if remain:
        def make_min_num():
            cnt = 0
            while True:
                for i in range(length-1, -1, -1):
                    if works[i] == 0:
                        if i == length-1:
                            return
                        break
                    cnt += 1
                    works[i] -= 1
                    if cnt == remain:
                        return
        make_min_num()

        for i in range(length-1, -1, -1):
            work = works[i]
            if work == 0:
                break
            answer += work * work
    return answer