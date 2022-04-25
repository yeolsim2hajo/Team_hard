input = 1
count = 0

for i in range(2, input) :
    if input%i == 0 :
        count+=1
    else :
        continue

if count > 0 or input == 1:
    print("NO")
else :
    print("YES")


# def prime(num) :
#     if num != 1 :
#         for i in range(2,num) :
#             if num%i == 0 :
#                 return False
#     else :
#         return False
#     return True

# sosu = 2

# if prime(sosu) :
#     print('YES')
# else :
#     print('NO')