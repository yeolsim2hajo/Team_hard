def main():
    arr = [3,5,1,2,7]
    target = list(map(int, input().split()))

    compareGo(arr, target)
    

def compareGo(arr1, arr2):
    if arr1 == arr2:
        print('두배열은완전같음')
    else:
        print('두배열은같지않음')

main()