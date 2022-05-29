
# 5의 배수가 될 때까지, 설탕의 무게에서 3킬로그램씩 빼기
kilo = int(input())
cnt = 0

while kilo >= 0:
    if kilo % 5 == 0:
        cnt += kilo // 5
        print(cnt)
        break
    
    kilo -= 3
    cnt += 1

else:
    print(-1)