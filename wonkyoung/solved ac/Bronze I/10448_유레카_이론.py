# 221122
# 삼각수 => 1 + ... + n = n(n+1)
# def main():

#     def triangle_num(number):
#         return number * (number + 1) // 2

#     def is_triangle_num(target):
#         for i in range(1, target+1):
#             first = triangle_num(i)
#             if first >= target:
#                 return 0
#             for j in range(i, target+1):
#                 second = triangle_num(j)
#                 number = first + second
#                 if number >= target:
#                     break
#                 for k in range(j, target+1):
#                     third = triangle_num(k)
#                     if number + third == target:
#                         return 1
#                     elif number + third > target:
#                         break
#         return 0

#     N = int(input())
#     for _ in range(N):
#         target = int(input())
#         print(is_triangle_num(target))
# main()




# 시간 더 걸림
# def main():

#     def fill_triangle_num(target):
#         for i in range(1, target):
#             number = i * (i+1) // 2
#             if number < target:
#                 triangle_num_list.append(number)
#             else:
#                 return triangle_num_list

#     def is_triangle_num(number=0, level=0):
#         nonlocal possible
#         if possible:
#             return
#         if level == 3:
#             if number == target:
#                 possible = 1
#             return
#         for i in triangle_num_list:
#             if number < target:
#                 is_triangle_num(number + i, level+1)
            
#     N = int(input())
#     for _ in range(N):
#         target = int(input())
#         possible = 0
#         triangle_num_list = []
#         fill_triangle_num(target)
#         is_triangle_num()
#         print(possible)
# main()


# comb 사용
def main():

    def fill_triangle_num(target):
        for i in range(1, target):
            number = i * (i+1) // 2
            if number < target:
                triangle_num_list.append(number)
            else:
                return triangle_num_list

    def is_triangle_num(number=0, level=0):
        nonlocal possible
        if possible:
            return
        if level == 3:
            if number == target:
                possible = 1
            return
        for i in triangle_num_list:
            if number < target:
                is_triangle_num(number + i, level+1)
            
    N = int(input())
    for _ in range(N):
        target = int(input())
        possible = 0
        triangle_num_list = []
        fill_triangle_num(target)
        is_triangle_num()
        print(possible)
main()