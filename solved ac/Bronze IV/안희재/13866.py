lst = list(map(int,input().split()))

lst.sort()

print(abs(lst[0]+lst[3]-lst[1]-lst[2]))