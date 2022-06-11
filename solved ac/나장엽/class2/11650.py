# 이차원 평면 위의 점 n개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하라

N = int(input())
point = []
for _ in range(N):
    point.append(input().split())


point.sort(key = lambda p : (int(p[1]), int(p[0])))
for i in range(N):
    print(point[i][0], point[i][1])