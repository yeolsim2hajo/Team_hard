a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
c1, c2 = map(int, input().split())

len_ab = (abs(b1-a1)**2+abs(b2-a2)**2)
len_bc = (abs(b1-c1)**2+abs(b2-c2)**2)
len_ac = (abs(c1-a1)**2+abs(c2-a2)**2)

length = [len_ab, len_bc, len_ac]
length2 = [len_ab**0.5, len_bc**0.5, len_ac**0.5]

length.sort()
length2.sort()
d = (length[0] + length[1])

tri = []
if length2[2] >= length2[1] + length2[0]:
    tri.append('X')
else:
    if length2[0] == length2[1] and length2[1] == length2[2]:
        tri.append('Jung')
    elif length2[0] == length2[1] or length2[1] == length2[2] or length2[2] == length2[0]:
        if d < length[2]:
            tri.append('Dunkak')
        elif d == length[2]:
            tri.append('Jikkak')
        else:
            tri.append('Yeahkak')
        tri.append('2')
    else:
        if d < length[2]:
            tri.append('Dunkak')
        elif d == length[2]:
            tri.append('Jikkak')
        else:
            tri.append('Yeahkak')
    tri.append('Triangle')

print(''.join(tri))