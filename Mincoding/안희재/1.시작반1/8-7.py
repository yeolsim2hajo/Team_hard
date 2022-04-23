arr1 = ['B','D','5','Q','A']
arr2 = ['Q','E','R','E','F']
tmp = ['HGFEDCBA']

def Input():
    str = input()
    if str.isupper() == 1:
        print(*arr2,sep='')
    elif str.islower() == 1:
        print(*arr1,sep='')
    else:
        print(*tmp)

Input()