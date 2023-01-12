#220928
X = int(input())
length = 64
rods = [64]
cnt = 1
while length > X:
    min_rod = min(rods)
    rods.remove(min_rod)
    min_rod //= 2
    length -= min_rod
print(cnt)