
n = input()
def cycle(n):
    cnt = 0
    new_n = 0

    if int(n) < 10:
        n = '0' + n
    
    temp = n
    while True:

        if new_n == n :
            return cnt
        Sum = 0
        for i in temp:
            Sum += int(i)

        if len(str(Sum)) == 1:
            new_n = temp[1] + str(Sum)
        else:
            new_n = temp[1] + str(Sum)[-1]

        temp = new_n
        cnt += 1


print(cycle(n))