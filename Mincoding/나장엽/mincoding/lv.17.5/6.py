password = [3,7,4,9]
input = list(map(int, input().split()))

def isSame(password, input):
    result = 0
    for i in range(4):
        if password[i] == input[i]:
            result = 1
        else:
            result = 0
            
    return result


if isSame(password, input):
    print('pass')
else:
    print('fail')