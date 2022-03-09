a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
b1 = int(input())
b2 = int(input())

print(sum([a1,a2,a3,a4]) - min(a1,a2,a3,a4) + max(b1,b2))

# sum(a1,a2,a3,a4) : TypeError: sum() takes at most 2 arguments (4 given)
# -> 리스트로 바꿔줘야 함
# -> 아니 그게 무제가 아니지.. list함수잖아
# -> 숫자는 iterable하지 않아서 적용할 수가 없음