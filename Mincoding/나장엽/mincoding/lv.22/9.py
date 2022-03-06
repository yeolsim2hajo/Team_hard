# 암호표에 암호문들이 있다. 
pw = [["Jason"],["Dr.tom"],["EXEXI"],["GK12P"],["POW"]]

input_pw = input()

result = 0

for i in range(len(pw)):
    if pw[i][0] == input_pw:
        result = 1
        break
    else:
        result = 0

if result :
    print("암호해제")
else:
    print("암호틀림")