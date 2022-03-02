vect = ["B","T","K","I","G","Z"]
target = list(input().split())


# 입력받은 target 중 몇 개의 알파벳이 vect 리스트에 있는지 출력하라
# target과 vect를 비교하여 일치하면 카운트를 증가시키고 출력

cnt = 0
for str in vect:
    for value in target:
        if str == value:
            cnt += 1

print(cnt)