def KFC():
    a = int(input())
    return a

def BBQ():
    if KFC() > 5:
        print('만세')
    else:
        print('다시')

BBQ()