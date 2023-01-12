#221011
formula = input()
start = 0
numbers, calc = [], []
for i in range(1, len(formula)):
    element = formula[i]
    if element in {'-', '+'}:
        numbers.append(int(formula[start:i]))
        calc.append(element)
        start = i+1
numbers.append(int(formula[start:]))

if calc.count('-'):
    half = len(calc)//2 + 1
    for i in range(half):
        for _ in range(i):



