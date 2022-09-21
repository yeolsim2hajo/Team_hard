s = input()
length = len(s)
index = 0
arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in arr:
    cnt = s.count(i)
    length -= cnt * len(i)
    index += 1 * cnt
    s = s.replace(i, ' ')

print(length + index)