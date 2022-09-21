#220918
N = int(input())
def find_total(limit):
    import sys
    total = 0
    new_input = sys.stdin.readline
    for _ in range(limit):
        total += int(new_input()) - 1
    return total + 1
print(find_total(N))