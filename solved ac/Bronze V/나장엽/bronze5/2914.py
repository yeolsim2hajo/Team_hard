cnt, avg = list(map(int, input().split(' ')))
result = 0
if cnt == 1:
    result = cnt*avg
else:
    result = ((avg-1)*cnt)+1 

print(result)