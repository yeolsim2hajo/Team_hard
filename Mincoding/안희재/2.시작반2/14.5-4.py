A = {'딸기':300, '메론':500, '수박':1000}
B = {'딸기':450, '메론':450, '수박':900}
C = {'딸기':200, '메론':150, '수박':700}

word = input()
if word == 'A':
    print(sum(list(A.values()))//3)
elif word == 'B':
    print(sum(list(B.values()))//3)
else:
    print(sum(list(C.values()))//3)

