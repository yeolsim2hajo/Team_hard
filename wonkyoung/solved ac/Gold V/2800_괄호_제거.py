#230210
# formula = list(map(str, input()))
# open, close = [], []
# length = len(formula)
# element_len = 0
# left, right = -1, length
# while left < right:
#     while left < right:
#         left += 1
#         if formula[left] == '(': break
#     else:
#         break
#     open.append(left)
#     element_len += 1
#     while left < right:
#         right -= 1
#         if formula[right] == ')': break
#     close.append(right)
#
# formula_list, path = [], []
# def dfs(level=0, start=0):
#     if level == cnt:
#         new_formula = formula[:]
#         for open_i, close_i in path:
#             new_formula[open_i] = new_formula[close_i] = ''
#         formula_list.append(''.join(new_formula))
#         return
#     for i in range(start, element_len):
#         path.append((open[i], close[i]))
#         dfs(level+1, i+1)
#         path.pop()
#
# for cnt in range(1, element_len+1):
#     dfs()
#
# formula_list.sort()
# print(*formula_list, sep='\n')


#230211
# 틀림
# def remove_brackets():
#     formula = list(map(str, input()))
#     open_symbol, close_symbol = [], []
#     length = len(formula)
#     open_len = 0
#     def cnt_brackets():
#         nonlocal open_len
#         left, right = 0, length-1
#         while left < right:
#             if formula[left] == '(':
#                 open_len += 1
#                 open_symbol.append(left)
#                 while left < right:
#                     if formula[right] == ')':
#                         close_symbol.append(right)
#                         break
#                     right -= 1
#             elif formula[right] == ')':
#                 close_symbol.append(right)
#                 while left < right:
#                     if formula[left] == '(':
#                         open_len += 1
#                         open_symbol.append(left)
#                         break
#                     left += 1
#             left += 1
#             right -= 1
#     cnt_brackets()
#     formula_list, path = [], []
#
#     def dfs(level=0, start=0):
#         if level == cnt:
#             new_formula = formula[:]
#             for open_i, close_i in path:
#                 new_formula[open_i] = new_formula[close_i] = ''
#             formula_list.append(''.join(new_formula))
#             return
#         for i in range(start, open_len):
#             path.append((open_symbol[i], close_symbol[i]))
#             dfs(level+1, i+1)
#             path.pop()
#
#     for cnt in range(1, open_len+1):
#         dfs()
#     formula_list.sort()
#     return formula_list
# print(*remove_brackets(), sep='\n')

#
# def remove_brackets():
#     formula = list(map(str, input()))
#     open_symbol, brackets = [], []
#     length = len(formula)
#     def cnt_brackets():
#         for i in range(length):
#             if formula[i] == '(':
#                 open_symbol.append(i)
#             elif formula[i] == ')':
#                 open_i = open_symbol.pop()
#                 brackets.append((open_i, i))
#     cnt_brackets()
#     formula_list, path = set(), []
#     bracket_cnt = len(brackets)
#     def dfs(level=0, start=0):
#         if level == cnt:
#             new_formula = formula[:]
#             for open_i, close_i in path:
#                 new_formula[open_i] = new_formula[close_i] = ''
#             formula_list.add(''.join(new_formula))
#             return
#         for i in range(start, bracket_cnt):
#             path.append(brackets[i])
#             dfs(level+1, i+1)
#             path.pop()
#
#     for cnt in range(1, bracket_cnt+1):
#         dfs()
#     formula_list = sorted(formula_list)
#     return formula_list
# print(*remove_brackets(), sep='\n')
'''
(1+2)*(3+4)
(((1+2))+(3*4)/7)*3
'''

#
# def remove_brackets():
#     formula = list(map(str, input()))
#     brackets = []
#     length = len(formula)
#     def cnt_brackets():
#         open_symbol = []
#         for i in range(length):
#             if formula[i] == '(':
#                 open_symbol.append(i)
#             elif formula[i] == ')':
#                 open_i = open_symbol.pop()
#                 brackets.append((open_i, i))
#     cnt_brackets()
#     formula_list, path = set(), []
#     bracket_cnt = len(brackets)
#     def dfs(level=0, start=0):
#         if level == cnt:
#             new_formula = formula[:]
#             for open_i, close_i in path:
#                 new_formula[open_i] = new_formula[close_i] = ''
#             formula_list.add(''.join(new_formula))
#             return
#         for i in range(start, bracket_cnt):
#             path.append(brackets[i])
#             dfs(level+1, i+1)
#             path.pop()
#
#     for cnt in range(1, bracket_cnt+1):
#         dfs()
#     formula_list = sorted(formula_list)
#     return formula_list
# print(*remove_brackets(), sep='\n')


#
def remove_brackets():
    formula = list(map(str, input()))
    brackets = []
    length = len(formula)
    def cnt_brackets():
        open_symbol = []
        for i in range(length):
            if formula[i] == '(':
                open_symbol.append(i)
            elif formula[i] == ')':
                open_i = open_symbol.pop()
                brackets.append((open_i, i))
    cnt_brackets()

    formula_list, path = set(), []
    bracket_cnt = len(brackets)
    def dfs(level=0, start=0):
        if path:
            new_formula = formula[:]
            for open_i, close_i in path:
                new_formula[open_i] = new_formula[close_i] = ''
            formula_list.add(''.join(new_formula))
            if level == bracket_cnt:
                return
        for i in range(start, bracket_cnt):
            path.append(brackets[i])
            dfs(level+1, i+1)
            path.pop()
    dfs()
    formula_list = sorted(formula_list)
    return formula_list
print(*remove_brackets(), sep='\n')



