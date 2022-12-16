#221216
def to_int(number):
    return int(''.join(number.split(':')))

def is_clock_num(number):
    global option
    number = str(number).rjust(6, '0')
    if not ('00' <= number[-2:] <= '59'):
        option = 1
        return False
    if not ('00' <= number[-4:-2] <= '59'):
        option = 2
        return False
    if not ('00' <= number[-6:-4] <= '23'):
        option = 3
        return False
    return True

def to_next_num(number):
    if option == 1:
        number += 40
    elif option == 2:
        number += 4000

    str_number = str(number).rjust(6, '0')
    if not ('00' <= str_number[-4:-2] <= '59'):
        number += 4000
    return number

def find_cnt(start, end):
    number, cnt = start, 0
    while number <= end:
        if is_clock_num(number):
            if number % 3 == 0:
                cnt += 1
            number += 1
        else:
            number = to_next_num(number)
    return cnt

for _ in range(3):
    start, end = input().split()
    start, end = to_int(start), to_int(end)
    option = 0
    if start <= end:
        cnt = find_cnt(start, end)
    else:
        cnt = find_cnt(start, 235959)
        cnt += find_cnt(0, end)
    print(cnt)


