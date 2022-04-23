def input_func():
    return input()

def main():
    a, b, c = map(int, input_func().split())
    calc(a,b,c)

def calc(arg1, arg2, arg3):
    print(arg1 + arg2 + arg3)

main()