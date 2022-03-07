num = list(map(int,input().split()))
arr = [num[0]] * 5
arr2 = [num[1]] * 5

def PrintAll():
    print(''.join(map(str,arr)))
    print(''.join(map(str,arr2)))

PrintAll()

# 아. 처음에 print(''.join(arr)) 만 했지..
# join함수는 문자열만 적용 가능함...
