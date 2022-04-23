def KFC():
    word = input()
    cnt_l = 0
    cnt_u = 0
    for ele in word:
        if ele.islower():
            cnt_l += 1
        if ele.isupper():
            cnt_u += 1
    
    print(f'대문자{cnt_u}개')
    print(f'소문자{cnt_l}개')

def main():
    KFC()

main()