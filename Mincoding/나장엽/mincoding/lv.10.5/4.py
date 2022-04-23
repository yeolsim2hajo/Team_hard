arr = [['D','A','C','C','D'],['S','D','F','A','E'],['E','E','T','J','H']]

def check(str):
    flag = 0
    for i in range(3):
        for k in range(5):
            if arr[i][k] == str:
                flag = 1
    return flag

def Input():
    str = input()
    return str

def main():
    a = Input()
    if check(a):
        print("있음")
    else:
        print("없음")

main()