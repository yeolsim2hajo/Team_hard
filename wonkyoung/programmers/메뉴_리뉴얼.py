#221002
def solution(orders, course):
    from collections import defaultdict
    answer = []
    max_cnt = course[-1]
    course_len = [set() for _ in range(max_cnt + 1)]
    course = set(course)
    match = defaultdict(int)
    def dfs(set_menu, start, level=1):
        if level > max_cnt:
            return
        if level in course:
            match[set_menu] += 1
            course_len[level].add(set_menu)
        for j in range(start, length):
            if visited[j] == 0:
                visited[j] = 1
                dfs(set_menu+order[j], j+1, level+1)
                visited[j] = 0
    for order in orders:
        order = sorted(order)
        length = len(order)
        for i in range(length):
            visited = [0] * length
            visited[i] = 1
            dfs(order[i], i+1)
    for i in course:
        max_order = 2
        menu_list = []
        for key in course_len[i]:
            if max_order < match[key]:
                menu_list = [key]
                max_order = match[key]
            elif max_order == match[key]:
                menu_list.append(key)
        answer.extend(menu_list)
    answer.sort()
    return answer

'''
테스트 1 〉	통과 (0.15ms, 10.1MB)
테스트 2 〉	통과 (0.09ms, 10.2MB)
테스트 3 〉	통과 (0.15ms, 10.3MB)
테스트 4 〉	통과 (0.14ms, 10.2MB)
테스트 5 〉	통과 (0.14ms, 10.2MB)
테스트 6 〉	통과 (0.40ms, 10.3MB)
테스트 7 〉	통과 (0.46ms, 10.3MB)
테스트 8 〉	통과 (8.60ms, 10.4MB)
테스트 9 〉	통과 (3.56ms, 10.2MB)
테스트 10 〉	통과 (7.86ms, 10.6MB)
테스트 11 〉	통과 (2.44ms, 10.5MB)
테스트 12 〉	통과 (4.12ms, 10.6MB)
테스트 13 〉	통과 (4.51ms, 10.7MB)
테스트 14 〉	통과 (4.61ms, 10.2MB)
테스트 15 〉	통과 (8.74ms, 10.6MB)
테스트 16 〉	통과 (8.18ms, 10.3MB)
테스트 17 〉	통과 (5.04ms, 10.2MB)
테스트 18 〉	통과 (7.02ms, 10.2MB)
테스트 19 〉	통과 (6.28ms, 10.4MB)
테스트 20 〉	통과 (5.87ms, 10.3MB)
'''