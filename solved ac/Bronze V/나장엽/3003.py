lost_pieces = list(map(int, input().split(" ")))
pieces = [1,1,2,2,2,8]
result = []
for i in range(len(pieces)):
    result.append(pieces[i]-lost_pieces[i])
print(result)