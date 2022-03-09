str = input()

if ord('A') <= ord(str) <= ord('Z'):
    print('대문자입니다')
elif ord('a') <= ord(str) <= ord('z'):
    print('소문자입니다')