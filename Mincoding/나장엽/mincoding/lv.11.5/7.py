arr = [['a','b','d'],['e','w','z'],['q','v','a']]

def Input():
    str = input()
    return str

def Process(str, arr):
    flag = 0
    str = str.lower()
    for i in range(3):
        for k in range(3):
            if arr[i][k] == str:
                flag = 1
    if flag:
        print('존재')
    else:
        print('없음')

def main():
    Process(Input(), arr)

main()