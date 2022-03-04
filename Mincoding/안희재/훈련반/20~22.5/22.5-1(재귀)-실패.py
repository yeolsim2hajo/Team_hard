arr = [ [['A','T','B'],['C','C','B']], [['A','A','A'],['B','B','C']] ]

# 아. arr[0][0][0] 이렇게 인덱스 총 3개인데, 이게 card 느낌이네
word = input()
card = [0, 1, 2]
path = [''] * 3

def abc(level):
    if level == 3:
        if arr[path[0]][path[1]][path[2]] == word:
            print('발견')
            return
        return

    for i in range(3):
        path[level] = card[i]
        abc(level+1)

abc(0)
# 이게 아닌데... arr의 첫번째와 두번째 []부분은 0,1만 있잖아..