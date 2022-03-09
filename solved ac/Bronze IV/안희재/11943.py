# 총 4개의 숫자 중에서, 제일 작은거(min) 선택 -> 
# 그거 + , 반대편 크로스 숫자(0번인덱스면 다른 상자 1번인덱스 / 1번인덱스면 다른 상자 0번인덱스)
# a, b = map(int, input().split())
# c, d = map(int, input().split())

# num1 = min(a,b,c,d)
# num2 = 0

# if num1 == a:
#     num2 = d
# elif num1 == b:
#     num2 = c
# elif num1 == c:
#     num2 = b
# else:
#     num2 = a

# print(num1+num2)
# 이렇게 풀면 2,3 / 2,2인 경우 오류 생김. min은 2인데, 어떤 2를 선택하냐에 따라 답이 5가 될 수 있음

# 하.. 그냥 대각선 합구해서 더 작은 수 고르면 되잖아..
a, b = map(int, input().split())
c, d = map(int, input().split())

print(min(a+d, b+c))