# 리모컨 버튼 0 ~ 9
# + 를 누르면 채널 +1
# - 를 누르면 채널 -1
# 채널 0에서 - 를 누르면 채널 이동 x 
# 채널은 0 ~ 무한대
# 이동하려는 채널은 N, 어떤 버튼이 고장났는지 주어졌을 때,
# 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야하는지 구하라


# import sys
# input = sys.stdin.readline

# def dfs(level):
#     if level == len(str(N)):
#         channel = ''
#         for i in range(len(str(N))):
#             channel += str(make_channels[i])
#         channels.append(int(channel))
#         return 

#     for i in range(len(remain)):
#         make_channels[level] = remain[i]
#         dfs(level+1)

# N = int(input())
# M = int(input())
# buttons = [i for i in range(0, 10)]

# if M != 0:
#     broke = list(map(int, input().split())) # 망가진 리모컨 버튼
#     remain = []
#     for i in range(10):
#         if buttons[i] in broke:
#             continue 
#         else:
#             remain.append(buttons[i])
# else:
#     remain = buttons[:]

# make_channels = ['']*len(str(N))
# channels = []

# dfs(0)

# Min = 19949949494949
# index = 0
# for i in range(len(channels)):
#     if Min > abs(N - channels[i]):
#         Min = abs(N - channels[i])
#         index = i

# Max = channels[index]
# count = abs(N - Max) + len(str(Max))

# if N == 100:
#     print(0)
# else:
#     print(count)



def dfs(level):
    global Min, make_channel
    global answer 
    if level == len(N):
        channel = int(''.join(map(str, make_channel)))
        Min = min(Min, abs(int(N) - channel) + len(str(channel)))
        return
    for i in range(10):
        if not broke[i]:
            make_channel.append(i)
            dfs(level+1)
            make_channel.pop()

    
N = input()
M = int(input())
broke = [False]*10
if M > 0:
    for i in list(map(int, input().split())):
        broke[i] = True

Min = abs(int(N) - 100)

make_channel = []
dfs(0)
print(Min)