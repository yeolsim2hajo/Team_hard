# 모듈 쓰는 방법 -> 당장에는 쓸 일이 없지만, 알아둬서 나쁠 건 없을 것

from itertools import permutations # "이 문제에서는 안쓰지만 어떤 것인지 확인해보세요."
from itertools import combinations

import itertools

user_input = input().split(',')
user_input_int = int(input())

#print(list(itertools.combinations(a, 3)))

print(list(map(''.join, combinations(user_input, user_input_int))))