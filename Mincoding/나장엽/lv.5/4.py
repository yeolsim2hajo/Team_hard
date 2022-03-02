def kfc():
    print('KFC입니다')
    
    
def mc():
    print('MC입니다')
    
n = int(input())

if n == 1:
    kfc()
else:
    mc()
    
# !none을 출력하기 싫다면 함수만 호출..! none이 출력되는 이유는 함수에 리턴값이 없으면 자동으로 none을 반환하기 때문이다.
# !따라서 출력만을 이용하고 싶다면 print(kfc())는 x! just kfc()
