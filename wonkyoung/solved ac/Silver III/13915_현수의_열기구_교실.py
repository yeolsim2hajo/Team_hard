#221219
# import sys
# new_input = sys.stdin.readline
# while True:
#     N = new_input().rstrip()
#     if not N:
#         break
#     N = int(N)
#     kind = []
#     for _ in range(N):
#         balloon = set(map(str, new_input().rstrip()))
#         for each in kind:
#             if balloon == each:
#                 break
#         else:
#             kind.append(balloon)
#     print(len(kind))


# 함수로
# def main():
#     import sys
#     new_input = sys.stdin.readline
#     def kind_cnt(students):
#         kind = []
#         for _ in range(students):
#             balloon = set(map(str, new_input().rstrip()))
#             for each in kind:
#                 if balloon == each:
#                     break
#             else:
#                 kind.append(balloon)
#         return len(kind)
#     while True:
#         N = new_input().rstrip()
#         if not N:
#             return
#         print(kind_cnt(int(N)))
# main()

# set, tuple
def main():
    import sys
    new_input = sys.stdin.readline
    def kind_cnt(students):
        kind = set()
        for _ in range(students):
            balloon = tuple(sorted(set(map(str, new_input().rstrip()))))
            kind.add(balloon)
        return len(kind)
    while True:
        N = new_input().rstrip()
        if not N:
            return
        print(kind_cnt(int(N)))
main()