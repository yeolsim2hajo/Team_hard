# 36진법 0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

# 36진법의 수 n개가 주어진다
# 둘 째 줄부터 n개의 줄에 수가 주어진다
# n은 최대 50이고 수의 길이도 최대 50 
# 마지막 줄에 k가 주어진다. k는 36보다 작거나 같은 자연수 또는 0


# 골드 1문제...ㅂㄷㅂㄷ...


# 36진법 숫자 중에서 k개의 숫자를 고른다. 그리고 나서 n개의 수 모두에서 나타난 그 숫자를 z르 바꾼다. 
# 그 이후에 n개의 수 를 모두 더한다

n = int(input())
number = []
for _ in range(n):
    number.append(input())
k = int(input())


number36 = [i for i in range(0, 10)]
number36.extend([chr(i) for i in range(65, 91)])

print(number36)