#230204
# N = int(input())
# if N%2:
#     answer = 'SK'
# else:
#     answer = 'CY'
# print(answer)


#

def rock_game():
    from sys import stdin
    new_input = stdin.readline
    N = int(new_input())
    return 'SK' if N%2 else 'CY'
print(rock_game())