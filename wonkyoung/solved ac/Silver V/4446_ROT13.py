#230128
# vowel = 'aiyeou'
# consonant = 'bkxznhdcwgpvjqtsrlmf'
# converted_alp = {}
# for i in range(6):
#     converted_alp[vowel[i]] = vowel[i-3] if i >= 3 else vowel[i+3]
# for i in range(20):
#     converted_alp[consonant[i]] = consonant[i-10] if i >= 10 else consonant[i+10]
# def to_upper(alp):
#     return alp.upper()
# keys = vowel + consonant
# for key in keys:
#     value = converted_alp[key]
#     converted_alp[key.upper()] = value.upper()
#
# while True:
#     try:
#         rot13 = input()
#         english = ''
#         for alp in rot13:
#             if converted_alp.get(alp):
#                 english += converted_alp[alp]
#             else:
#                 english += alp
#         print(english)
#     except:
#         break






def print_english():
    def fill_dict():
        vowel = 'aiyeou'
        consonant = 'bkxznhdcwgpvjqtsrlmf'
        for i in range(6):
            converted_alp[vowel[i]] = vowel[i - 3] if i >= 3 else vowel[i + 3]
        for i in range(20):
            converted_alp[consonant[i]] = consonant[i - 10] if i >= 10 else consonant[i + 10]
        keys = vowel + consonant
        for key in keys:
            value = converted_alp[key]
            converted_alp[key.upper()] = value.upper()

    def find_english(rot13):
        english = ''
        for alp in rot13:
            if converted_alp.get(alp):
                english += converted_alp[alp]
            else:
                english += alp
        return english

    converted_alp = {}
    fill_dict()
    while True:
        try:
            rot13 = input()
            print(find_english(rot13))
        except:
            return
print_english()


def print_english():
    vowel = 'aiyeou'
    consonant = 'bkxznhdcwgpvjqtsrlmf'
    converted_alp = {}
    for limit, arr in (6, vowel), (20, consonant):
        num = limit//2
        for i in range(limit):
            key = arr[i]
            value = arr[i-num] if i >= num else arr[i+num]
            converted_alp[key] = value
            converted_alp[key.upper()] = value.upper()

    while True:
        try:
            rot13 = input()
            english = ''
            for alp in rot13:
                if converted_alp.get(alp):
                    english += converted_alp[alp]
                else:
                    english += alp
            print(english)
        except:
            return
print_english()


#
def print_english():
    converted_alp = {}
    for limit, num, arr in (6, 3, 'aiyeou'), (20, 10, 'bkxznhdcwgpvjqtsrlmf'):
        for i in range(limit):
            key = arr[i]
            value = arr[i-num] if i >= num else arr[i+num]
            converted_alp[key] = value
            converted_alp[key.upper()] = value.upper()

    while True:
        try:
            rot13 = input()
            english = ''
            for alp in rot13:
                if converted_alp.get(alp):
                    english += converted_alp[alp]
                else:
                    english += alp
            print(english)
        except:
            return
print_english()