def main():
    num = int(input())
    arr =  [num + i for i in range(6)]
    return arr

def PrintAll():
    for i in main():
        print(i)

PrintAll()