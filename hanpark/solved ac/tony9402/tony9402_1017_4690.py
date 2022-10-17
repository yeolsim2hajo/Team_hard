# 백준 4690 완전 세제곱

for a in range(2,101):
    for b in range(2,101):
        for c in range(b+1,101):
            for d in range(c+1,101):
                if a*a*a==(b*b*b+c*c*c+d*d*d):
                    print("Cube = {}, Triple = ({},{},{})".format(a,b,c,d))
                if a*a*a<(b*b*b+c*c*c+d*d*d):break