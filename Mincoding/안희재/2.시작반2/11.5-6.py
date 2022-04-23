arr = [['a','b','E'], ['E','2','W'], ['3','2','4']]
# int형 세기 귀찮아서 그냥 다 문자형식으로 만듦

for i in range(3):
    for j in range(3):
        if arr[i][j].islower() == 0 and arr[i][j].isupper() == 0: # 대,소문자 아니면 숫자형 문자
            print(int(arr[i][j])+5, end= ' ')
        elif arr[i][j].islower() == 1:
            print(arr[i][j].upper(), end= ' ')
        elif arr[i][j].isupper() == 1:
            print(arr[i][j].lower(), end= ' ')
    print()