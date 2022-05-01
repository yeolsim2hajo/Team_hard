#10171 고양이
# print('\\    /\\')
# print(' )  ( \')')
# print('(  /  )')
# print(' \\(__)|')

'''
\    /\
 )  ( ')
(  /  )
 \(__)|
'''

#10172 개
# print('|\\_/|')
# print('|q p|   /}')
# print('( 0 )"""\\')
# print('|"^"`    |')
# print('||_/=\\\\__|')

'''
|\_/|
|q p|   /}
( 0 )"""\
|"^"`    |
||_/=\\__|
'''

#10809 알파벳 찾기
S = input()
alphabet = [-1]*26
for i in range(len(S)):
    idx = ord(S[i])-ord('a')
    if alphabet[idx] == -1:
        alphabet[idx] = i
print(*alphabet)

