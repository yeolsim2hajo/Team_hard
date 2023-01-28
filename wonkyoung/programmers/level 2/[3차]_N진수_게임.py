#230128
def solution(n, t, m, p):
    if n > 10:
        over_ten = {i+10:chr(65+i) for i in range(6)}
    total_len, cnt, start = 0, 0, p-1
    total = answer = ''

    def conv_num(target, num):
        if target <= 1:
            return (str(target), 1)
        result, length = '', 0
        while target:
            remain = target%num
            if remain < 10:
                result = str(remain) + result
            else:
                result = over_ten[remain] + result
            target //= num
            length += 1
        return (result, length)

    num = 0
    while True:
        result, length = conv_num(num, n)
        total += result
        total_len += length
        while start < total_len-1:
            answer += total[start]
            cnt += 1
            start += m
        if cnt >= t:
            print(answer)
            return answer[:t]
        num += 1
solution(2, 4, 2, 1)
solution(16, 16, 2, 1)
solution(16, 16, 2, 2)
