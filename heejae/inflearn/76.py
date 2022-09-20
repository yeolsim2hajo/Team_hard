a, b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(a)]

Max = 0
for i in range(a-b+1):
	Sum = 0
	for j in range(a-b+1):
		Sum += sum(arr[0+i+j][0+j:2+j])
	if Max < Sum:
		Max = Sum

print(Max)