arr1 = ['B','D','5','Q','A']
arr2 = ['Q','E','R','E','F']


def fn():
    str = input()
    return str

def output(str):
    if str.islower() :
        print(''.join(arr1))
    elif str.isupper() : 
        print(''.join(arr2))
    else:
        print('HGFEDCBA')


output(fn())