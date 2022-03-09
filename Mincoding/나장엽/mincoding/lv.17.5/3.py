name1 = input()
name2 = input()

def isSame(name1, name2):
    if name1 == name2:
        return 1
    else:
        return 0

if isSame(name1, name2):
    print("동명")
else:
    print("남남")