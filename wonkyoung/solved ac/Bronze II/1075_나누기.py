#221103
N = int(input()[:-2] + '00')
F = int(input())
remain = N%F
if remain:
    remain = F - remain
if remain < 10:
    remain = '0' + str(remain)
print(remain)


#
def find_number():
    N = int(input()[:-2] + '00')
    F = int(input())
    remain = N%F
    if remain == 0:
        return '00'
    remain = F - remain
    if remain >= 10:
        return remain
    remain = '0' + str(remain)
    return remain
print(find_number())