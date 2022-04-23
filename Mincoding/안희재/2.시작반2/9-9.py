arr = [['F','E','W'], ['D','C','A']]

def main():
    str = input()
    return str

def findch(str):
    result = '미발견'
    for i in range(2):
        for j in range(3):
            if arr[i][j] == str:
                result = '발견'
                return result
            else:
                continue
    return result

print(findch(main()))