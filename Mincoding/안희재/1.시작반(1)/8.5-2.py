arr = ['D','T','A','B','W','Q']

word = input()

for i in range(len(arr)):
    if arr[i] == word:
        print(f'{i}번 INDEX')