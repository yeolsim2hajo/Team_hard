D, H, M = map(int,input().split())

# 11일 11시간 11분
if D == 11 and H == 11 and M <= 10:
    print(-1)
elif D == 11 and H <= 10:
    print(-1)
elif D <= 10:
    print(-1)
else:
    print(D*1440 + H * 60 + M - 16511) # 11일, 11시, 11분 -> 16651

# 이렇게 하면, 12:4:1 vs 11:11:11 계산 복잡하게 안해도 됨
# 기준점보다 H,M이 작은 경우 그 상위 시간에서 하나 빼고 해야되잖슴

# 어 음 근데..
# D, H, M = map(int, input().split())
# t1 = D*24*60 + H*60 + M
# t2 = 11*24*60 + 11*60 + 11
# t = t1 - t2
# if t < 0:
#     print(-1)
# else:
#     print(t)
# 이게 더 나은것 같기도 하고..? 일단, 이 방법도 기억해두자