#1110 더하기 사이클
N = int(input())
plus = sum(divmod(N,10)) if N >= 10 else N
number = str(N%10) + str(plus%10)
cycle = 1
while True:
    if int(number) == N:
        break
    number = number[-1]
    plus = sum(divmod(int(number), 10)) if N >= 10 else N
    number += str(plus)[-1]
    cycle += 1
print(cycle)




# word = input()
# for alp in word:
#     print(alp.swapcase(), end='')