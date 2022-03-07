arr = ['#','_','#','_','#','#']

result = ''
for ele in arr:
    if ele == '#':
        result += '샵'
    else:
        result += '무'

print(result)