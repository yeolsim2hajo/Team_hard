x = int(input())
count = 0
n = 64
while x > 0:
	if n > x:
		n = n // 2
	else:
		count += 1
		x -= n
print(count)