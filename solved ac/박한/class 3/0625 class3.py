# class 3++ 1541 잃어버린 괄호

inp = input().split('-')
rst = 0
for i in inp[0].split('+'):
    rst += int(i)
for i in inp[1:]:
    lst = i.split('+')
    for j in lst:
        rst -= int(j)
print(rst)