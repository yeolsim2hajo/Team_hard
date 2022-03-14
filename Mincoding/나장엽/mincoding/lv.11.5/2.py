arr = [[1,1,1],[1,2,1],[3,6,3]]

def count(arr, n):
    cnt = 0
    for i in range(3):
        for k in range(3):
            if arr[i][k] == n:
                cnt += 1
    return cnt

def main():
    n = int(input())
    print(count(arr, n))
    