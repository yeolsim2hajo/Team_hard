#230219
def find_length():
    from sys import stdin
    new_input = stdin.readline
    N, M = map(int, new_input().split())
    root_of = list(range(N+1))
    def find(node):
        if node == root_of[node]:
            return node
        root = find(root_of[node])
        root_of[node] = root
        return root
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u == root_v:
            return
        elif root_u < root_v:
            root_of[root_v] = root_u
        else:
            root_of[root_u] = root_v

    for _ in range(M):
        u, v = map(int, new_input().split())
        union(u, v)

    root_set = set()
    for node in range(1, N+1):
        find(node)
        root = root_of[node]
        root_set.add(root)

    return len(root_set)

print(find_length())
'''
6 7
1 2
2 4
3 2
5 3
4 6
5 6
5 4

11 8
1 3
2 4
5 8
6 7
9 11
4 3
7 8
11 10
'''
