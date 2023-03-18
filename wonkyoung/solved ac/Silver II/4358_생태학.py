#220814
# 틀림
# def calc_ratio():
#     from sys import stdin
#     new_input = stdin.readline
#     total = 0
#     species = {}
#     while True:
#         tree = new_input().rstrip()
#         if not tree:
#             keys = sorted(species)
#             print(keys)
#             for key in keys:
#                 print(key, round(species[key] / total * 100, 4))
#             return
#         if species.get(tree):
#             species[tree] += 1
#         else:
#             species[tree] = 1
#         total += 1
#
# calc_ratio()

#230318
# from sys import stdin
# new_input = stdin.readline
# trees = {}
# total = 0
# while True:
#     tree = new_input().rstrip()
#     if not tree:
#         break
#     total += 1
#     if trees.get(tree):
#         trees[tree] += 1
#     else:
#         trees[tree] = 1
# for tree in sorted(trees):
#     print(f'{tree} {trees[tree]*100/total :.4f}')


#
# from sys import stdin
# new_input = stdin.readline
# trees = {}
# total = 0
# while True:
#     tree = new_input().rstrip()
#     if not tree:
#         break
#     total += 1
#     if trees.get(tree):
#         trees[tree] += 1
#     else:
#         trees[tree] = 1
# for tree in sorted(trees):
#     print(tree, f'{trees[tree]*100/total :.4f}')


#
# def calc_ratio():
#     from sys import stdin
#     new_input = stdin.readline
#     trees = {}
#     total = 0
#     while True:
#         tree = new_input().rstrip()
#         if not tree:
#             break
#         total += 1
#         if trees.get(tree):
#             trees[tree] += 1
#         else:
#             trees[tree] = 1
#     for tree in sorted(trees):
#         print(tree, f'{trees[tree]*100/total :.4f}')
# calc_ratio()



#
# def calc_ratio():
#     from sys import stdin
#     from collections import defaultdict
#     new_input = stdin.readline
#     trees = defaultdict(int)
#     total = 0
#     while True:
#         tree = new_input().rstrip()
#         if not tree:
#             for tree in sorted(trees):
#                 print(tree, f'{trees[tree] * 100 / total :.4f}')
#             return
#         total += 1
#         trees[tree] += 1
#
# calc_ratio()


#
# def calc_ratio():
#     from sys import stdin
#     new_input = stdin.readline
#     trees = {}
#     total = 0
#     while True:
#         tree = new_input().rstrip()
#         if not tree:
#             break
#         total += 1
#         if trees.get(tree):
#             trees[tree] += 1
#         else:
#             trees[tree] = 1
#     visited = {}
#     for tree in sorted(trees):
#         value = trees[tree]
#         if not visited.get(value):
#             visited[value] = value*100/total
#         print(tree, f'{visited[value] :.4f}')
# calc_ratio()


#
def calc_ratio():
    from sys import stdin
    new_input = stdin.readline
    trees = {}
    total = 0
    while True:
        tree = new_input().rstrip()
        if not tree:
            break
        total += 1
        if not trees.get(tree):
            trees[tree] = 1
        else:
            trees[tree] += 1
    for tree in sorted(trees):
        print(tree, f'{trees[tree]*100/total :.4f}')
calc_ratio()