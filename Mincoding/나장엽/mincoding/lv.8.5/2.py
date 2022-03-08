arr = ['D','T','A','B','W','Q']

str = input()


idx = 0
for i in range(len(arr)):
    if arr[i] == str:
        print(f'{i}번 INDEX')
