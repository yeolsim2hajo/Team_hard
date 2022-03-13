def Input():
    n = list(map(int, input().split()))
    return n

def main():
    n = Input()
    calc(n)
def calc(list):
    result = 0
    for i in list:
        result += i
    print(result)

main()