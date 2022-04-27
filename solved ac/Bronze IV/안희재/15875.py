numbers = input()
# A,B는 1부터 10까지의 자연수
# 37, 102, 1010, 910의 4가지 경우를 모두 만족시킬 수 있어야 함
if len(numbers) == 2:
    print(int(numbers[0])+int(numbers[1]))
elif len(numbers) == 4:
    print(20)
else: # 3인경우 -> 102, 910이 각각 12, 19가 나와야 함
    if numbers[1] == '0': # 102
        print(int(numbers[0:2])+int(numbers[-1]))
    else: # 910
        print(int(numbers[0])+int(numbers[1:]))

