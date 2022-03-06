a, b = map(int, input().split())

arr1 = ['']*5
for i in range(5):
    arr1[i] = a
arr2 = ['']*5
for k in range(5):
    arr2[k] = b
    
    
def printAll():
    for i in range(5):
        print(arr1[i], end='')
    print()
    for k in range(5):
        print(arr2[k], end='')
        
printAll()