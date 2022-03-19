n = int(input())

cnt = 0
for i in range(n+1):
    i = str(i)
    for j in i:
        if j == '1':
            cnt += 1

print(cnt)

# 아래코드 훨씬 보기 좋네 ㄷㄷ;;
# def count(n):
# 	countN = str(list(range(n+1))).count('1')
# 	return countN

# print(count(1000))