#221004
import sys

new_input = sys.stdin.readline
H, W = map(int, new_input().split())
N = int(new_input())
stickers = [list(map(int, new_input().split())) for _ in range(N)]
max_area = 0
def calc_area(arr1, arr2):
    return arr1[0] * arr1[1] + arr2[0] * arr2[1]

def find_max(arr1, arr2):
    for width, height in (H, W), (W, H):
        for i in range(2):
            for j in range(2):
                if arr1[i] + arr2[j] <= width and max(arr1[1-i], arr2[1-j]) <= height:
                    return calc_area(arr1, arr2)
    return 0

for i in range(N-1):
    for j in range(i+1, N):
        max_area = max(find_max(stickers[i], stickers[j]), max_area)
print(max_area)
