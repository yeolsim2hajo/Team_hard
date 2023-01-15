#230115
def solution(babbling):
    answer = 0
    okay = {'aya','ye', 'woo', 'ma'}
    for each in babbling:
        i = 0
        before = ''
        while i < len(each):
            two, three = each[i:i+2], each[i:i+3]
            if two in okay and before != two:
                before = two
                i += 2
            elif three in okay and before != three:
                before = three
                i += 3
            else:
                break
        else:
            answer += 1
    return answer