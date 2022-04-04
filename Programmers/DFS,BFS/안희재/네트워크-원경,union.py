def network(number):
    if check[number] == '':
        return number
    ret = network(check[number])
    check[number] = ret
    return ret

def union(a,b):
    global answer
    n_a, n_b = network(a),network(b)
    if n_a == n_b:
        return 1
    check[n_a] = n_b

def solution(n, computers):
    global answer,check
    answer = n
    check = ['']*n
    if n !=1:
        for i in range(n):
            for j in range(i+1,n):
                if computers[i][j] == 1:
                    if union(i,j) != 1:
                        answer -= 1
    else:
        answer = 1
    return answer