# 라이브러리 사용법 -> 다시 사용해보기
from itertools import permutations

number = input()
n = int(input())
arr = [i for i in number]

print(max(list(map(''.join, permutations(arr, n)))))

