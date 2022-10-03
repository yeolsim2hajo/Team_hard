# 백준 20154 이 구역의 승자는 누구야?!

import sys
input = sys.stdin.readline

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '32123333113133122212112221'
rst = 0
a = input().strip()
for i in range(len(a)):
    rst += int (numbers[alphabet.index(a[i])])
    rst %= 10
if rst % 2 == 0:
    print("You're the winner?")
else:
    print("I'm a winner!")