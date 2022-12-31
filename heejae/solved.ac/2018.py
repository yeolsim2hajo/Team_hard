n = int(input())
start, end = 1, 1
cnt, total = 0, 1

while end != n:
    if total < n:  # 합이 n보다 작으면 뒤에 수 추가
        end += 1
        total += end
    elif total > n:  # 합이 n보다 크면 앞에 수 빼기
        total -= start
        start += 1
    else:  # 합이 n과 같으면
        cnt += 1
        end += 1
        total += end

print(cnt + 1)  # 자기 자신도 포함