def Sum(lst):
    result = 0
    result = lst[0] + lst[1]
    return result
def comp(lst):
    result = 0 
    result = lst[0] - lst[1]
    return result

def Print(a, b):
    print(f'합:{a}')
    print(f'차:{b}')

def main():
    lst = list(map(int, input().split()))
    a = Sum(lst)
    b = comp(lst)
    Print(a, b)

main()

