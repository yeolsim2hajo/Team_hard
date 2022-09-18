arr =[['F','E','W'],['D','C','A']]

def main():
    str = input()
    return str
def findCh(str, arr):
    flag = 0
    for i in range(2):
        for k in range(3):
            if arr[i][k] == str:
                flag = 1
    if flag == 1:
        print("발견")
    else:
        print("미발견")

findCh(main(), arr)