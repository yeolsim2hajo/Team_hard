# 변수 a, b, c에 숫자를 각각 1개씩 입력 받아라
# a~b
# a~c 까지 출력하는 소스코드를 작성해라

a, b, c = map(int, input().split())
temp = a
for i in range(b-a+1):
    print(a, end=' ')
    a += 1
print()
a = temp
for j in range(c-a+1):
    print(a, end=' ')
    a += 1