str = input()

if ord('a') <= ord(str) <= ord('z'):
    print('소문자입력!!')
    
elif ord('A') <= ord(str) <= ord('Z'):
    print('대문자입력!!')
    
elif ord('0') <= ord(str) <= ord('9'):
    print('숫자문자입력!!')