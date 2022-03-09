# 숫자 2개를 입력 받고 큰  숫자가  어떤 숫자인지 알려주는 프로그램
# 예시) 3, 5를 입력받으면 큰  수는 5
# 같은 수를 입력하면 같은 숫자.   

n1, n2 = map(int, input().split())

if n1 and n2 != 0:
    if n1 > n2: 
        print("큰수는 {}".format(n1))
    else:
        print("큰수는 {}".format(n2))


if n1 == n2:
    print("같은숫자")