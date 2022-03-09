arr = [[15,18,17], [4,6,9], [10,1,3], [7,8,9], [15,2,6]]
arr = arr[::-1]

def isPattern(lst):
    family = list(map(int,input().split()))
    answer = ''
    for i in range(len(lst)):
        if family == lst[i]:
            answer = (f'{i+1}층')
    return answer

print(isPattern(arr))