def main():
    a=GOP()
    b=SUM()
    if a > b:
        print("GOP>SUM")
    elif a == b:
        print("GOP==SUM")
    else:
        print("GOP<SUM")
    
def GOP():
    n1, n2 = map(int, input().split())
    result = 0
    result = n1*n2
    return result
    
def SUM():
    n1, n2 = map(int, input().split())
    result = 0
    result = n1+n2
    return result


main()