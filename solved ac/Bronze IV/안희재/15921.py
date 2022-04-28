# 문제는 매우 간단해서 중요한건 아님. 포인트는 2가지
    # 소수점 2자리까지 표현
    # 0일때는 입력값이 1줄이고, 아닐때는 2줄이라는 것임 -> 이걸 표현하는 방법 아래처럼! 매우 중요!!!!
        # 나 원래 이런거 안된다고 생각했었음 ㅅㅂ;;;
N = int(input())
if N == 0:
    print('divide by zero')
else:
    records = list(map(int,input().split()))
    avg = sum(records)//N
    expect = sum(records)//N
    result = avg/expect
    print("%.2f" % result)