def atoz():
    word = input()
    if ord(word) - 65 > 90 - ord(word):
        return 'Z'
    else:
        return 'A'

def main():
    print(atoz())

main()