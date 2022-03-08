arr = [['A','B','C','D','E'], ['F','G','H','I','J'], ['K','L','M','N','O'], ['P','Q','R','S','T'], ['U','V','W','X','Y']]
word = input()

word_x = 0
word_y = 0

for i in range(5):
    for j in range(5):
        if word == arr[i][j]:
            word_x = i
            word_y = j

print(f'{word_x-2},{word_y-2}')