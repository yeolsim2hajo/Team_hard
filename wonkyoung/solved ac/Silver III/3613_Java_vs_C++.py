#230324
# var_name = input()
# def convert_other():
#     if not var_name[0].islower():
#         return 'Error!'
#     new_var = ''
#     length = len(var_name)
#     for i in range(length):
#         element = var_name[i]
#         if not element.isalpha():
#             if element == '_':
#                 is_java = False
#                 apply_rule = True
#                 break
#             else:
#                 return 'Error!'
#         elif element.isupper():
#             is_java = True
#             new_var += f'_{element.lower()}'
#             apply_rule = False
#             break
#         else:
#             new_var += element
#     else:
#         return new_var
#
#     for j in range(i+1, length):
#         element = var_name[j]
#         if element.islower():
#             if apply_rule:
#                 new_var += element.upper()
#                 apply_rule = False
#             else:
#                 new_var += element
#         elif is_java and element.isupper():
#             new_var += f'_{element.lower()}'
#         elif not is_java and element == '_':
#             if apply_rule:
#                 return 'Error!'
#             apply_rule = True
#         else:
#             return 'Error!'
#     return 'Error!' if apply_rule else new_var
# print(convert_other())


#
def convert_other():
    var_name = input()
    if not var_name[0].islower():
        return 'Error!'
    new_var = ''
    length = len(var_name)
    mode = 0
    apply_rule = False
    for i in range(length):
        element = var_name[i]
        if not element.isalpha():
            if element == '_':
                if mode == 0:
                    mode = 1
                elif mode == 2 or apply_rule:
                    return 'Error!'
                apply_rule = True
            else:
                return 'Error!'
        elif element.isupper():
            if mode == 0:
                mode = 2
            elif mode == 1:
                return 'Error!'
            new_var += f'_{element.lower()}'
        elif apply_rule:
            new_var += element.upper()
            apply_rule = False
        else:
            new_var += element
    return 'Error!' if apply_rule else new_var
print(convert_other())