# 백준 21756 지우개

import sys
from math import log2
input = sys.stdin.readline

N = log2(int(input()))
print(int(2**int(N)))