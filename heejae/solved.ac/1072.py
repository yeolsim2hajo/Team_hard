import sys
input = sys.stdin.readline

x, y = map(int, input().rsplit())
victory = y * 100 // x
ans = sys.maxsize
l, r = 1, x
print("[victory]:", victory)

while l <= r:
    mid = (l + r) // 2

    curr_vic = (y + mid) * 100 // (x + mid)
   
    if curr_vic > victory:
        ans = min(mid,ans)
        r = mid - 1
    else:
        l = mid + 1

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)