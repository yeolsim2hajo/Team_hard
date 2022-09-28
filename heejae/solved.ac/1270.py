import sys

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    land = list(map(int, input().split()))
    land.sort()

    left = right = 0
    answer = []
    while right < len(land):
        if land[left] == land[right]:
            right += 1
        else:
            answer.append((right-left, land[left]))
            left = right
    answer.append((right - left, land[left]))
    answer.sort()

    cnt, army = answer[-1]
    if cnt >= len(land)/2:
        print(army)
    else:
        print("SYJKGW")
출처: https://hello-i-t.tistory.com/109 [저녁 하늘의 종이 비행기:티스토리]