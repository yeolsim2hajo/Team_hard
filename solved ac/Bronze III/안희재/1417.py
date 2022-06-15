import sys
 
input = sys.stdin.readline
 
n = int(input())
vote_list = []
count = 0
 
for i in range(n):
    vote_list.append(int(input()))
if n == 1:
    print(0)
else:
    dasom = vote_list[0]
    not_dasom = sorted(vote_list[1:], reverse=True)
    for index, num in enumerate(not_dasom):
        if dasom == num:
            print(1)
            break
        while(not_dasom[0] >= dasom):
            count += 1
            dasom += 1
            not_dasom[0] -= 1
            not_dasom = sorted(not_dasom, reverse=True)
        print(count)
        break