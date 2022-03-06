nums = list(map(int, input().split()))


for num in nums:
    if num < 20:
        print('더 큰수를 입력하세요')
    elif num > 20:
        print('더 작은수를 입력하세요')
    else:
        print('정답입니다')
        