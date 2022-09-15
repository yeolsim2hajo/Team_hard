 # 어떤 수 x가 주어졌을 때, x의 모든 자리수가 역순이 된 수를 얻을 수 있다.
 # Rev(x)를 x의 모든 자리수를 역순으로 만드는 함수라고 하자.
 # 예를 들어 x = 123일때 rev(x) = 321
 # x = 100 일때, rev(x)  = 0

def rev(number):
    number = number[::-1]
    return number

data = list(input().split())
print(data)
print(int(rev(str(int(rev(data[0])) + int(rev(data[1]))))))



