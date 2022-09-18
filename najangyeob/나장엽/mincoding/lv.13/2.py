def moom(n):
    lst = []
    a = n - 4
    b = n + 3
    c = n*2
    lst.append(a)
    lst.append(b)
    lst.append(c)

    return lst

def main():
    n = int(input())
    a = moom(n)
    print(*a, sep= ' ')

main()