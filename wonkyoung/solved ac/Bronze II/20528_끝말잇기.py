#230306
def link_word():
    N = int(input())
    words = input().split()
    first = words[0][0]
    for i in range(1, N):
        if not words[i].startswith(first):
            return 0
    return 1
print(link_word())