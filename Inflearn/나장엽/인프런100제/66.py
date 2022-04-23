arr = ['ABCDEF', 'BCAD', 'ADEFQRX', 'BEDFG', 'AEBFDGCH']
target = 'ABCD'

def check(lst, target):
    temp = target.index(target[0])
    for i in lst:
        if i in target:
            if temp > target.index(i):
                return False
            temp = target.index(i)
            
    return True

def func(arr, target):
    answer = []
    for i in arr:
        answer.append(check(i, target))
        
    return answer

print(func(arr, target))