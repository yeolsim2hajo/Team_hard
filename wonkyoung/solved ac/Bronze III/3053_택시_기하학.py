#230306
# from math import pi
# radius = int(input())
# print(round(pi * radius * radius, 6))
# print(f'{2*radius*radius:.6f}')

#
# from math import pi
# radius = int(input())
# print(f'{pi * radius * radius:.6f}')
# print(f'{2*radius*radius:.6f}')

#
# from math import pi
# radius = int(input())
# print(f'{pi * radius * radius:.6f}\n{2*radius*radius:.6f}')

#
def calc_area():
    from math import pi
    radius = int(input())
    square = radius * radius
    return f'{pi * square:.6f}\n{2*square:.6f}'
print(calc_area())