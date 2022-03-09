password = [3,7,4,9]

input_arr = list(map(int,input().split()))

def isSame(lst):
    if password == lst:
        return 'pass'
    else:
        return 'fail'

print(isSame(input_arr))