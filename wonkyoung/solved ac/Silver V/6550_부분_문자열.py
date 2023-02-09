#230209
# def find_answer():
#     from sys import stdin
#     new_input = stdin.readline
#     alp_list = []
#     for i in range(26):
#         alp_list.append(chr(i + 97))
#         alp_list.append(chr(i + 65))
#
#     def is_contained():
#         s, t = new_input().rstrip().split()
#         alp_location = {alp_list[i]: -1 for i in range(52)}
#         length = len(t)
#         for i in range(length):
#             alp = t[i]
#             if alp_location.get(alp) == -1:
#                 alp_location[alp] = [i]
#             else:
#                 alp_location[alp].append(i)
#         before = -1
#         for alp in s:
#             if alp_location.get(alp, -1) != -1:
#                 locations = alp_location[alp]
#                 for location in locations:
#                     if location > before:
#                         before = location
#                         break
#                 else:
#                     return 'No'
#             else:
#                 return 'No'
#         return 'Yes'
#
#     while True:
#         try:
#             print(is_contained())
#         except Exception:
#             return
# find_answer()


#
# def find_answer():
#     from sys import stdin
#     new_input = stdin.readline
#
#     def is_contained():
#         s, t = new_input().rstrip().split()
#         s_length, t_length = len(s), len(t)
#         s_i = t_i = 0
#         alp_s, alp_t = s[s_i], t[t_i]
#         while t_i < t_length:
#             alp_t = t[t_i]
#             if alp_s == alp_t:
#                 s_i += 1
#                 if s_i == s_length:
#                     return 'Yes'
#                 alp_s = s[s_i]
#             t_i += 1
#         return 'No'
#
#     while True:
#         try:
#             print(is_contained())
#         except Exception:
#             return
# find_answer()


#
# def find_answer():
#     def is_contained():
#         s, t = input().split()
#         s_length, t_length = len(s), len(t)
#         s_i = t_i = 0
#         alp_s, alp_t = s[s_i], t[t_i]
#         while t_i < t_length:
#             alp_t = t[t_i]
#             if alp_s == alp_t:
#                 s_i += 1
#                 if s_i == s_length:
#                     return 'Yes'
#                 alp_s = s[s_i]
#             t_i += 1
#         return 'No'
#
#     while True:
#         try:
#             print(is_contained())
#         except Exception:
#             return
# find_answer()

#
# def find_answer():
#     def is_contained():
#         s, t = input().split()
#         s_length = len(s)
#         s_i, alp_s = 0, s[0]
#         for alp_t in t:
#             if alp_s == alp_t:
#                 s_i += 1
#                 if s_i == s_length:
#                     return 'Yes'
#                 alp_s = s[s_i]
#         return 'No'
#
#     while True:
#         try:
#             print(is_contained())
#         except Exception:
#             return
# find_answer()


#
# def find_answer():
#     from sys import stdin
#     new_input = stdin.readline
#     def is_contained(s, t):
#         s_length = len(s)
#         s_i, alp_s = 0, s[0]
#         for alp_t in t:
#             if alp_s == alp_t:
#                 s_i += 1
#                 if s_i == s_length:
#                     return 'Yes'
#                 alp_s = s[s_i]
#         return 'No'
#
#     while True:
#         input_str = new_input().rstrip()
#         if input_str:
#             print(is_contained(*input_str.split()))
#         else:
#             return
# find_answer()

#
def find_answer():
    from sys import stdin
    new_input = stdin.readline
    def is_contained(s, t):
        t_length, start = len(t), 0
        for alp_s in s:
            if start == t_length:
                return 'No'
            for i in range(start, t_length):
                if alp_s == t[i]:
                    start = i+1
                    break
            else:
                return 'No'
        return 'Yes'

    while True:
        input_str = new_input().rstrip()
        if input_str:
            print(is_contained(*input_str.split()))
        else:
            return
find_answer()