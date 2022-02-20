# 숫자 2개를 입력받아라 (두 번째숫자는 첫 번째 숫자보다 크다.)
# 첫 번째 숫자부터 두 번째 숫자 값까지 출력해라

n1, n2 = map(int, input().split())

for i in range(n1, n2+1):
    print(i)