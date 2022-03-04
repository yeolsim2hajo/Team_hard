word = input()
arr1 = [chr(ord(word)+i) for i in range(0,5)]
arr2 = [chr(ord(word)-i) for i in range(0,5)]

print(*arr1,sep='')
print(*arr2,sep='')