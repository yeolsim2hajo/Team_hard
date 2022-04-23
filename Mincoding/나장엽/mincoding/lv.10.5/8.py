def main():
    a = Calculator()
    print(a)
def Calculator():
    score = int(input())
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'D'
main()