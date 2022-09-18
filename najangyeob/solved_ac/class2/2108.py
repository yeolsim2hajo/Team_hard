import sys
from collections import Counter
input = sysinput = sys.stdin.readline


N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))
length = N

Sum = sum(numbers)

numbers.sort()
numbers_maxcount = Counter(numbers).most_common()

Max = max(numbers)
Min = min(numbers)

print(round(Sum/N)) # 산술평균
print(numbers[length//2]) # 중앙값
if len(numbers_maxcount) > 1:
    if numbers_maxcount[0][1] == numbers_maxcount[1][1]:
        print(numbers_maxcount[1][0])
    else:
        print(numbers_maxcount[0][0])
else:
    print(numbers_maxcount[0][0])

print(abs(Max - Min))