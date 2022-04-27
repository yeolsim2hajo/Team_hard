arr = []
for i in range(3):
    arr.append(int(input()))

gop = 1
for i in range(3):
    gop = gop * (arr[i])

gop = str(gop)
dat = [0]*10

# 0 0 0 0 0 0 0 0 0 0
for i in range(len(gop)):
    dat[int(gop[i])] += 1

for i in dat:
    print(i)