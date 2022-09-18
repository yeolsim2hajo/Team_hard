user_id = 'qlqlaqkq'
user_pw = 'tkaruqtkf'

ID = input()
pw = input()
cnt= 0


def abc(level, i):
    global cnt

    if level == len(user_id):
        if cnt == 1:
            print('LOGIN')
        else:
            print('INVALID')
        return

    if user_id[i] == ID[i]:
        cnt = 1
    else:
        cnt = 0
    if user_pw[i] == pw[i]:
        cnt = 1
    else:
        cnt = 0

    abc(level+1, i+1)
abc(0, 0)