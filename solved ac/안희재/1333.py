if __name__ == '__main__':
    n, l, d = map(int, input().split())
    check = [False] * (n * l + 5 * (n - 1))

    for i in range(n):
        s = (l + 5) * i
        for j in range(s, s + l):
            check[j] = True

    answer = 0
    while answer < len(check):
        if not check[answer]:
            break
        answer += d
    print(answer)