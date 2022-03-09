def FindABC(x,y):
    CA, CB, CC = 0, 0, 0 # counting A

    for ele in x:
        if ele == 'A':
            CA += 1
        if ele == 'B':
            CB += 1
        if ele == 'C':
            CC += 1

    for ele in y:
            if ele == 'A':
                CA += 1
            if ele == 'B':
                CB += 1
            if ele == 'C':
                CC += 1
    
    return CA,CB,CC

def main():
    word1 = input()
    word2 = input()
    print(f'A:{FindABC(word1,word2)[0]}')
    print(f'B:{FindABC(word1,word2)[1]}')
    print(f'C:{FindABC(word1,word2)[2]}')

main()