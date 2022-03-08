arr = [ [['A','T','B'],['C','C','B']], [['A','A','A'],['B','B','C']] ]

word = input()

def check():
    answer = '미발견'
    for i in range(2):
        for j in range(2):
            for k in range(3):
                if arr[i][j][k] == word:
                    answer = '발견'
                    return answer

    return answer

print(check())