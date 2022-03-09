arr = [4,1,2,3,5]

word = input()
if word == 'a' or word == 'b' or word == 'c':
    print(' '.join(map(str,arr[3::-1])))
else:
    print(' '.join(map(str,arr[4:0:-1])))