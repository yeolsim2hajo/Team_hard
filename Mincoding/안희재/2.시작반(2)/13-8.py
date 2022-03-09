def main():
    arr = [3,5,1,2,7]
    arr2 = list(map(int,input().split()))
    compareGo(arr,arr2)

def compareGo(ar1,ar2):
    if ar1 == ar2:
        print('두배열은완전같음')
    else:
        print('두배열은같지않음')

main()