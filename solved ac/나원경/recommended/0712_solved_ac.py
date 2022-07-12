#1972 놀라운 문자열
def main():
    import sys
    new_input = sys.stdin.readline
    def is_surprising():
        for i in range(1,n-1):
            arr = set()
            for j in range(n-i):
                new = data[j] + data[j+i]
                if new in arr:
                    return 0
                arr.add(new)
        return 1

    while True:
        data = new_input().rstrip()
        n = len(data)
        if data == '*':
            return
        if is_surprising():
            print(f'{data} is surprising.')
        else:
            print(f'{data} is NOT surprising.')
main()


