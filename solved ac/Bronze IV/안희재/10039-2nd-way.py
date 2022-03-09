sum = 0
for i in range(5):
    num = int(input())

    if num < 40:
        num = 40
    
    sum += num

print(sum//5)

# 이렇게 풀 수 있네 // 이러면 총 세로 5줄 각각 입력폼을 구현할 수 있음