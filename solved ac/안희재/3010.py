from sys import stdin

data = stdin.readline().rstrip()
s, i = '', 1


def check(s):
    t = list(s)
    k = list(data)

    while 1:
        if len(t) < len(data):
            return ' '

        else:
            i = 0
            chk = 0
            while 1:
                if i >= len(k) or i >= len(t):
                    if chk:
                        return ''.join(t)
                    else:
                        return ''.join(t[:len(data)])

                if t[i] != k[i]:
                    t.pop(i)
                    chk = 1
                else:
                    i += 1

while 1:
    s += str(i)

    # check
    tf = check(s)

    if tf[:min(len(tf), len(data))] == data:
        print(i)
        break

    # tf = False
    if tf != ' ':
        s = tf
        i += 1
    else:
        i += 1