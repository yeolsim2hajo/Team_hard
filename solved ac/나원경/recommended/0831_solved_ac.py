# resistance = {
#     'black':0,
#     'brown':1,
#     'red':2,
#     'orange':3,
#     'yellow':4,
#     'green':5,
#     'blue':6,
#     'violet':7,
#     'grey':8,
#     'white':9,
# }
# value = ''
# for _ in range(2):
#     value += str(resistance[input()])
# print(int(value) * 10** (resistance[input()]))

# resistance = {
#     'black':0,
#     'brown':1,
#     'red':2,
#     'orange':3,
#     'yellow':4,
#     'green':5,
#     'blue':6,
#     'violet':7,
#     'grey':8,
#     'white':9,
# }
# value = 0
# for i in range(2):
#     value += resistance[input()] * 10 ** (1-i)
# print(value * 10 ** (resistance[input()]))


resistance = {
    'black':0,
    'brown':1,
    'red':2,
    'orange':3,
    'yellow':4,
    'green':5,
    'blue':6,
    'violet':7,
    'grey':8,
    'white':9,
}
value = ''
for i in range(2):
    value += str(resistance[input()])
value += '0'*resistance[input()]
if value.startswith('0'):
    value = value[1:]
print(value)
