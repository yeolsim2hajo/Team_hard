#!/usr/bin/env python
# coding: utf-8

# In[9]:


# 백준 브론즈 5 2845번

A, B = map(int, input().split())
C = map(int, input().split())
H = A*B
for i in C:
    print(i-H, end= ' ')


# In[15]:


# 백준 브론즈 5 2914번

A, B = map(int, input().split())
if A == 1:
    print(A*B)
else:
    print(A*(B-1)+1)

# 올림해서 출력값이 나오려면, 예를 들어 뒷값이 24라면 23.00~01이라고 가정했을 때 저작권의 멜로디 최소값이 나오게 됨.
# 따라서 A*(B-1)을 해주고, 나머지인 0.00~01을 처리해주기 위해서 +1을 했음


# In[19]:


# 백준 브론즈 5 3003번

A, B, C, D, E, F = map(int, input().split())
G = ((1-A), (1-B), (2-C), (2-D), (2-E), (8-F))
for i in G:
    print(i, end = ' ')


# In[22]:


# 백준 브론즈 5 3046번

R1, S = map(int, input().split())
R2 = 2*S - R1
print(R2)


# In[25]:


# 백준 브론즈 5 5554번

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = A+B+C+D
print(E//60)
print(E%60)


# In[26]:


# 백준 브론즈 5 8370번
# 여기로 가져올만한 가치가 있는 문제가 정말 없다...

A, B, C, D = map(int, input().split())
print(A*B + C*D)


# In[29]:


# 백준 브론즈 5 8393번

A = int(input())
print(int(A*(A+1)/2))

