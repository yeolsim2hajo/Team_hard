towers = input().split()
rule = input()

for i in range(len(towers)):
    tmp = []
    for j in range(len(rule)):
        if rule[j] in towers[i]: # index함수는 이 경우 써줘야함. 없으면 아예 에러떠서;;
            tmp.append(towers[i].index(rule[j]))

    for j in range(len(tmp)-1):
        if tmp[j] > tmp[j+1]:
            print('불가능')
            break
    else:
        print('가능')




# ABCDEF BCAD ADEFQRX BEDFG