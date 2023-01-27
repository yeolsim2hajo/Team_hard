#230127
# import sys
#
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# dna_list = [new_input().rstrip() for _ in range(N)]
# neucleotide = 'ACGT'
# element = {alp: 0 for alp in neucleotide}
# haming_distance, final_dna = 0, ''
# for j in range(M):
#     each_element = dict(element)
#     for i in range(N):
#         each_element[dna_list[i][j]] += 1
#     each_cnt, each_key = 0, ''
#     for key in neucleotide:
#         if each_element[key] > each_cnt:
#             each_cnt = each_element[key]
#             each_key = key
#     final_dna += each_key
#     haming_distance += (N - each_cnt)
# print(final_dna, haming_distance, sep='\n')


# 정리
# def find_min_dna():
#     neucleotide = 'ACGT'
#     element = {alp: 0 for alp in neucleotide}
#     haming_distance, final_dna = 0, ''
#     for j in range(M):
#         each_element = dict(element)
#         each_cnt, each_key = 0, ''
#         for i in range(N):
#             each_element[dna_list[i][j]] += 1
#         for key in neucleotide:
#             if each_element[key] > each_cnt:
#                 each_cnt = each_element[key]
#                 each_key = key
#         final_dna += each_key
#         haming_distance += (N - each_cnt)
#     print(final_dna, haming_distance, sep='\n')
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# dna_list = [new_input().rstrip() for _ in range(N)]
# find_min_dna()


# 정리2
# def find_min_dna():
#     neucleotide, haming_distance, final_dna = 'ACGT', 0, ''
#     element = {alp: 0 for alp in neucleotide}
#     for j in range(M):
#         each_element = dict(element)
#         each_cnt, each_key = 0, ''
#         for i in range(N):
#             each_element[dna_list[i][j]] += 1
#         for key in neucleotide:
#             if each_element[key] > each_cnt:
#                 each_cnt, each_key = each_element[key], key
#         final_dna += each_key
#         haming_distance += (N - each_cnt)
#     print(final_dna, haming_distance, sep='\n')
#
# import sys
# new_input = sys.stdin.readline
# N, M = map(int, new_input().split())
# dna_list = [new_input().rstrip() for _ in range(N)]
# find_min_dna()

# 최소
def find_min_dna():
    neucleotide, haming_distance, final_dna = 'ACGT', 0, ''
    element = {alp: 0 for alp in neucleotide}
    for j in range(M):
        each_cnt, each_key = 0, ''
        for i in range(N):
            element[dna_list[i][j]] += 1
        for key in neucleotide:
            if element[key] > each_cnt:
                each_cnt, each_key = element[key], key
            element[key] = 0
        final_dna += each_key
        haming_distance += (N - each_cnt)

    print(final_dna, haming_distance, sep='\n')


import sys

new_input = sys.stdin.readline
N, M = map(int, new_input().split())
dna_list = [new_input().rstrip() for _ in range(N)]
find_min_dna()



# list
def find_min_dna():
    neucleotide, haming_distance, final_dna = 'ACGT', 0, ''
    element = [0] * 4
    for j in range(M):
        each_cnt, each_key = 0, ''
        for i in range(N):
            index = neucleotide.index(dna_list[i][j])
            element[index] += 1
        for i in range(4):
            if element[i] > each_cnt:
                each_cnt, each_key = element[i], neucleotide[i]
            element[i] = 0
        final_dna += each_key
        haming_distance += (N - each_cnt)

    print(final_dna, haming_distance, sep='\n')

import sys
new_input = sys.stdin.readline
N, M = map(int, new_input().split())
dna_list = [new_input().rstrip() for _ in range(N)]
find_min_dna()