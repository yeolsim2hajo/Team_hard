n, k = map(int, input().split())
arr = list()

for i in range(1, k+1):
	arr.append(int(str(n*i)[::-1])) # String으로 바꾼 후, 거꾸로 뒤집기

print(max(arr)); # max 출력