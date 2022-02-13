#!/usr/bin/env python
# coding: utf-8

# In[26]:


# 문자열 슬라이싱


letters = 'hello ssafy!'

# 3 번째 부터 7 번째 문자를 출력하세요

# 실행 예)
# llo s


# In[28]:


print(letters[2:7])


# In[29]:


# 문자열 인덱싱 [시작인덱스:끝인덱스:오프셋]


# 아래의 문자열에서 '데'만 출력하세요.

str = "데레데레데레"

print(str[0::2])


# In[ ]:


문자열 치환
아래의 전화번호에서 하이픈을 제거하고 출력하세요!

number = 010-1234-5678


# In[30]:


# 문자열은 immutable

# 아래 코드의 실행 결과를 예상해보세요

str = 'ssafy'
str[1] = 'A'
print(str)


# In[ ]:





# In[ ]:


# 문자열 출력
# % formatting 을 사용해서 다음과 같이 출력해라

name1 = '나장엽'
age1 = 31
name2 = '안희재'
age2 = 30

# 이름: 나장엽 나이: 31
# 이름: 안희재 나이: 30

print("이름: %s 나이: %d" % (name1, age1))


# In[ ]:


f-string을 사용하여 위의 문제를 다시 풀어보세요

name1 = '나장엽'
age1 = 31
name2 = '안희재'
age2 = 30

이름: 나장엽 나이: 31
이름: 안희재 나이: 30
        


# In[ ]:


print(f'이름: {name1} 나이: {age1})


# In[ ]:


리스트에 원소 추가 insert(인덱스, 원소)


twojo = ['나원경','안희재','박한','오서준']

나원경과 안희재 사이에 나장엽을 추가하세요


# In[ ]:


twojo.insert(1, '나장엽')


# In[ ]:


join 메서드

twojo = ['나원경','안희재','나장엽','오서준','박한'] 

아래와 같이 출력해라

1. 
    나원경/안희재/나장엽/오서준/박한
2.
    나원경
    안희재
    나장엽
    오서준
    박한

    
'/'.join(twojo)
'\n'.join(twojo)


# In[ ]:


stock = "lg에너지솔루션/대한항공/삼성전자/sk하이닉스"

stock 문자열을 하나의 리스트로 분리하여 저장하라

list1 = stock.split('/')


# In[ ]:


튜플 언팩킹

다음 코드의 실행 결과를 예상하라

fruits = ('apple','banana','watermelon')
a, b, c = fruits
print(a, b, c)


# In[ ]:


별 표현식

다음 코드의 실행 결과를 예상하라.

a, b, *c = (0,1,2,3,4,5,6)

print(a)
print(b)
print(c)


# In[ ]:


test_score 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 scores 변수에 넣어라~


test_score = [70,80,90,85,77,66,55,44,33,22]


# In[ ]:


test_score = [70,80,90,85,77,66,55,44,33,22]
*scores, _, _ = test_score
scores


# In[31]:


# 

# {"아이스크림이름":[가격, 재고]}

# icecreams 딕셔너리에서 메로나의 가격을 출력하세요~


icecreams = {
    "비비빅": [300, 20],
    "메로나": [500, 10],
    "누가바": [700, 10]
}


# In[ ]:


print(icecreams['메로나'][0])


# In[ ]:


# 딕셔너리 update 메서드

# 아래의 new_product 딕셔너리를 다음 icecream 딕셔너리에 추가해라

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)


# In[ ]:


파이썬 분기문
다음 결과를 예상하세요

print ((3 == 3) and (4 != 3))


# In[ ]:


#파이썬 분기문
#다음 결과를 예상하세요

if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")


# In[ ]:


# 다음 결과 값을 예상하세요

list1 = [1,2,3,4,5,6]
for i in list1[::-1]:
    print(i)


# In[ ]:


# 다음 결과 값을 예상하세요

list1 = [13, 21, 12, 14, 30, 18]
for i in list1:
    if (i < 20) and (i % 3 == 0):
        print(i)


# In[ ]:


# 다음 결과 값을 예상하세요


price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)


# In[ ]:


my_list = ["가", "나", "다", "라"] #i, i+1 i-1, i

아래와 같이 출력하는 코드를 작성하세요(? 채우기)

가 나
나 다
다 라


# In[ ]:


#방법 1.

for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1])
#방법 2.

for i in range( 1, len(my_list) ) :
    print(my_list[i-1], my_list[i])


# In[ ]:


my_list = ["가", "나", "다", "라"] # i, i-1 / 3- i, 2 - i

아래와 같이 출력하는 코드를 작성하세요(? 채우기)

라 다
다 나
나 가


# In[ ]:


#방법 1. 

for i in [3, 2, 1] :
    print(my_list[i], my_list[i-1])
    
#방법 2.

for i in [0, 1, 2] :
    print(my_list[3-i], my_list[2-i])

#방법 3.

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])


# In[ ]:


# 아래 코드의 출력결과를 예상하세요


apart = [ [101, 102], [201, 202], [301, 302] ]
#1.
for row in apart:
    for col in row:
        print(col, "호")
#2.        
for row in apart[::-1]:
    for col in row:
        print(col, "호")
        


# In[ ]:


# 아래 코드의 결과를 예상하세요

apart = [ [101, 102], [201, 202], [301, 302] ]
#1.
for row in apart:
    for col in row:
        print(col, "호")
        print("-" * 5)
#2.        
for row in apart:
    for col in row:
        print(col, "호")
    print("-----")


# In[32]:


# 아래의 에러가 발생하는 이유?

hellossafy()

def hellossafy():
    print("hello!")


# In[ ]:


실행 결과 예측!

def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()


# In[ ]:


#아래의 결과를 예상하세요~

def function(num):
    return num+5

a = function(10)
b = function(a)
c = function(b)

print(c)


# In[ ]:


class Human:
    pass

# human클래스의 인스턴스를 생성하고, jangyeob 변수에 할당하세요


# In[33]:


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

jangyeob = Human('나장엽', 31, '남자')

# 인스턴스 jangyeob의 나이를 출력하세요

print(jangyeob.age)


# In[34]:


class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        
        
    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex 
        
    def whoareyou(self):
        print("이름 : {0} 나이 : {1} 성별 : {2}".format(self.name, self.age, self.sex))
        
jangyeob = Human('모름', 0, '모름')
# 위의 클래스를 보고 jangyeob 인스턴스의 이름과 나이 성별을 다시 할당해주세요
# 여기에 코드를 추가하세요

jangyeob.setInfo('나장엽', 31, '남자')

jangyeob.whoareyou()






# In[ ]:


class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        
        
    #인스턴스에 이름을 입력 할 수 있는 set_name 메서드 코드를 작성하세요
    
    def set_name(self, name):
        self.name = name
    #인스턴스에 코드을 입력 할 수 있는 set_code 메서드 코드를 작성하세요
    
    def set_code(self. code):    
        self.code = code
    
    
a = Stock(None, None)
a.set_name("삼성전자") 
a.set_code("005930")
    
    
    


# In[ ]:


#다음 코드의 실행결과는?


class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")
        

나 = 자식()
나.호출()


# In[ ]:


#다음 코드의 실행결과는 ?

class 부모:
    def __init__(self):
        print("부모생성")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        
나 = 자식()


# In[ ]:


#다음 코드의 실행결과는?


class 부모:
      def __init__(self):
            print("부모생성")

class 자식(부모):
      def __init__(self):
            print("자식생성")
            super().__init__()

나 = 자식()


# In[ ]:


try:
    실행 코드
except:
    예외가 발생했을 때 수행할 코드
else:
    예외가 발생하지 않았을 때 수행할 코드
finally:
    예외 발생 여부와 상관없이 항상 수행할 코드

