word = input()
path = [[[0] * 3 for _ in range(3)] for _ in range(3)] # 오 ㅋ 걍 이렇게 하면 되는구나 3차원배열!

word_num = ord(word) # 'A'면 65가 출력

def abc(level):
    if level == 3:
        for i in range(3):
            for j in range(3):
                print(''.join(path[i][j]))
            print()
        return

    for i in range(3):
        for j in range(3):
            path[level][i][j] = chr(word_num+level) # word= 'A"면 -> level0에는 A가, level에는 B가!
    
    abc(level+1)

abc(0)

# 와 3차원 배열 이렇게 하면 되는구나 ㅋㅋㅋㅋㅋㅋㅋㅋ
# 내가 짰지만 대견스럽다 잘했다! 하핫