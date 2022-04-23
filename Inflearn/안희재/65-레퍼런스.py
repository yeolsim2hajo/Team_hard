# ---------------답
a = input().split(' ')
b = input().split(' ')

c = []
count = 0

for i, j in zip(a, b):
	if count % 2 == 0:
		c.append([i, j])
	else:
		c.append([j, i])
	count += 1

print(c)

# [[1,'a'],['b',2],[3,'c'],['d',4]]
# zip함수 ㄷㄷ; range대신에 zip!