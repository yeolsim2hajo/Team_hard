if __name__ == '__main__':
    n = int(input())
    player_list = []
    for _ in range(n):
        f = input()
        player_list.append(f[0])

    first_names = set(player_list)
    result = []
    for i in first_names:
        if player_list.count(i) >= 5:
            result.append(i)

    if len(result) > 0:
        print(''.join(sorted(result)))
    else:
        print("PREDAJA")