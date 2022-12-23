#221223
N, digit = input().split()
N = int(N)
cnt = 0
for i in range(1, N+1):
    number = str(i)
    for j in number:
        if j == digit:
            cnt += 1
print(cnt)


# 함수
def find_freq():
    N, digit = input().split()
    N, cnt = int(N), 0
    for i in range(1, N+1):
        number = str(i)
        for j in number:
            if j == digit:
                cnt += 1
    return cnt


# 붙이기 - 틀림 - 오류 처리 복잡 (나중에 다시)
def find_freq():
    from heapq import heappop, heappush
    N, digit = map(int, input().split())
    cnt = 1
    if N < digit:
        return 0
    length = len(str(N))
    str_digit = str(digit)
    numbers = '0123456789'
    heap = []
    for number in numbers:
        new_number = str_digit + number
        heappush(heap, (int(new_number), new_number))
        if number != str_digit:
            new_number = number + str_digit
            heappush(heap, (int(new_number), new_number))
    while True:
        now_int, now_str = heappop(heap)
        if not now_str.startswith('0'):
            cnt += 1
        if now_int > N:
            return cnt
        if length > len(now_str):
            for number in numbers:
                new_number = now_str + number
                heappush(heap, (int(new_number), new_number))
                if number != str_digit:
                    new_number = number + now_str
                    heappush(heap, (int(new_number), new_number))

print(find_freq())
