if __name__ == '__main__':
    cnt = 0
    while True:
        o, w = map(int, input().split())
        if o == 0 and w == 0:   # "0 0" 입력 시 모든 시나리오 끝남
            quit()

        die = False
        while True:
            action, n = input().split()
            if action == '#' and n == '0':
                break

            if not die:
                n = int(n)
                if action == 'E':
                    w -= int(n)
                elif action == 'F':
                    w += int(n)

            if w <= 0:  # 사망
                die = True

        cnt += 1
        if w <= 0:
            print("%d RIP" % cnt)
        elif o / 2 < w < o * 2:
            print("%d :-)" % cnt)
        else:
            print("%d :-(" % cnt)