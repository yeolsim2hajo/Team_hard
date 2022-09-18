# words = []
# while True:
#     word = input()

#     if word == '0':
#         break
#     else:
#         words.append(word)

# words = [list(word) for word in words]

# # reverse_words = []
# # for i in range(len(words)):
# #     reverse_words.append(list(reversed(words[i])))

# # for i in range(len(words)):
# #     if words[i] == reverse_words[i]:
# #         print('yes')
# #     else:
# #         print('no')


# for i in range(len(words)):
#     if words[i] == list(reversed(words[i])):
#         print('yes')
#     else:
#         print('no')

list_word = ['1', '2', '3']
tuple_word = ('1', '2', '3')
dict_word = {'t':'a', 'o':'c', 'p':'d'}
string_word = '123'


print(reversed(list_word))
print(reversed(tuple_word))
print(reversed(dict_word))
print(''.join(reversed(string_word)))

