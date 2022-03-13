def main():
    aToZ()
    
def aToZ():
    str = input()
    mid = (ord('Z') + ord('A'))//2
    if ord(str) - mid <= 0:
        print('A')
    else:
        print('Z')
main()