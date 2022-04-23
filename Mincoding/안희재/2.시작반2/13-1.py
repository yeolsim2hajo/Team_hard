def getName():
    a,b = input().split()
    return a,b

def main(tuple):
    print(chr(min(ord(tuple[0]),ord(tuple[1]))))

main(getName())