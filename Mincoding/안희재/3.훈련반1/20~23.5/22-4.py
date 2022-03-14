order = [input() for _ in range(5)] # 길이가 5인 배열

sum = 0
def abc(level):
    global sum
    if level == 5:
        if sum >= 0:
            print(sum+1)
        else:
            print(f'B{sum*-1}')
        return

    if order[level] == 'up':
        sum += 1
    else:
        sum -= 1
    
    abc(level+1)

abc(0)