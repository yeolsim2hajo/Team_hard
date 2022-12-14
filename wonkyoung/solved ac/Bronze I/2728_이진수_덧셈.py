#221214
def find_answer(one, two):

    def calc(one, two):
        len_one, len_two = len(one), len(two)
        if len_one > len_two:
            one, two = two, one
            len_one, len_two = len_two, len_one
        answer = ''
        next = False
        for i in range(-1, -len_one - 1, -1):
            if one[i] == two[i]:
                answer = '1' + answer if next else '0' + answer
                next = one[i] == '1'
            else:
                answer = '0' + answer if next else '1' + answer

        if len_one == len_two:
            if next:
                answer = '1' + answer
            return answer

        if next:
            for i in range(-len_one-1, -len_two-1, -1):
                if two[i] == '1':
                    answer = '0' + answer if next else '1' + answer
                else:
                    answer = '1' + answer if next else '0' + answer
                    next = False
            if next:
                answer = '1' + answer
        else:
            answer = two[:len_two-len_one] + answer
        return answer

    answer = calc(one, two)
    for i in range(len(answer)):
        if answer[i] == '1':
            return answer[i:]
    return '0'

import sys
new_input = sys.stdin.readline
T = int(new_input())
for _ in range(T):
    one, two = new_input().split()
    print(find_answer(one, two))

'''
3
0001010 0011
11111111 11
1011011 101
'''