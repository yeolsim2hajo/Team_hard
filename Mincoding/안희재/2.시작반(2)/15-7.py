arr = ['A','B','C','Z','E','T','Q']

black = input()

for i in range(5):
    result = '외부사람'
    for j in range(7):
        if black[i] == arr[j]:
            result = '마을사람'
            print(f'{black[i]}={result}')
            break
    else:
        print(f'{black[i]}={result}')
