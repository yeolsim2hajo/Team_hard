# 규칙을 찾아 아래와 같이 작동하는 프로그램을 만들어라
# 3을 입력하면 333 444 555

n = int(input())
# 풀이법 1
# for i in range(3):
#     print(n, end='')
# print()
# for i in range(3):
#     print(n+1, end='')
# print()
# for i in range(3):
#     print(n+2, end='')
# print()

# 풀이법 2
for i in range(3):
    n = n+1
    for k in range(3):
        print(n-1, end='')
    print()
