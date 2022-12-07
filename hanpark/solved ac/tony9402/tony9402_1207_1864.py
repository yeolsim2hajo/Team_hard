# 백준 1864 문어 숫자

import sys
input = sys.stdin.readline

while 1:
    a = input()
    if a == "#":
        break
    else:
        dict = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1, }
        l = len(a)
        rst = 0
        for i in range(l):
            rst += dict[a[i]] * (8 ** (l - i - 1))
        print(rst)