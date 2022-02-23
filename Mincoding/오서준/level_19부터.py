# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import sys
sys.stdin=open('tc.text')


#  #19-1.Direct 사용하기

# def Direct(arr,y,x):
#     dy=[-1,0,1,0]
#     dx=[0,1,0,-1]
#     sum1=0
#     for i in range(len(dy)):
#         if dy[i]+y>=0 and dx[i]+x>=0:
#             sum1+=arr[dy[i]+y][dx[i]+x]
#     return sum1
#
# arr=[[3,5,4],[1,1,2],[1,3,9]]
# y,x=map(int,input().split())
# print(Direct(arr,y,x))



# #19-4. 용의자의 GPS
#
# def Pprint(vect,gps):
#     for i in range(len(gps)):
#         vect[gps[i][0]][gps[i][1]] = 5
#     return vect
# gps=[list(map(int,input().split())) for _ in range(4)]
# vect=[[0]*3 for _ in range(4)]
# for i in range(len(vect)):
#     print(*Pprint(vect,gps)[i] )


# #19-5. 가장 큰곳 찾기
#
# def Max(map1):
#     dy=[-1,-1,1,1]
#     dx=[-1,1,1,-1]
#     max=0
#     InD=[]
#     for i in range(len(map1)):
#         for j in range(len(map1[i])):
#             sum1=0
#             for d in range(len(dy)):
#                 if len(map1)>dy[d]+i>=0 and len(map1[i])>dx[d]+j>=0:
#                     sum1+=map1[dy[d]+i][dx[d]+j]
#             if max<sum1:
#                 max=sum1
#                 InD = [i,j]
#     return InD
#
# map1=[[3,3,5,3,1],[2,2,4,2,6],[4,9,2,3,4],[1,1,1,1,1],[3,3,5,9,2]]
# print(*Max(map1))

# #19-6. 폭탄 투하
#
# def bomb(arr,b):
#     dy=[-1,-1,-1,0,1,1,1,0]
#     dx=[-1,0,1,1,1,0,-1,-1]
#     for i in range(len(dy)):
#         if len(arr)> dy[i]+b[0]>=0 and len(arr[0])> dx[i]+b[1]>=0:
#             arr[dy[i]+b[0]][dx[i]+b[1]]= '#'
#     return arr
#
# arr=[['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_'],['_','_','_','_','_']]
# B=[list(map(int,input().split())) for _ in range(2)]
# for b in range(len(B)):
#     arr=bomb(arr,B[b])
# for i in range(len(arr)):
#     print(*arr[i])



#19-7. sigma 이미지 프로세싱

# def Max(image):
#     sum1=0
#     max=0
#     Idex=[]
#     for i in range(len(image)-1):
#         for y in range(3):
#             sum1+= image[i][y]+image[i+1][y]
#
#         for j in range(len(image[i])-2):
#             if max<sum1:
#                 max=sum1
#                 Idex=[i,j]
#             if len(image[i])==j+3:
#                 break
#             sum1+=image[i][j+3]+image[i+1][j+3]-image[i][j]-image[i+1][j]
#     return Idex
#
# image = [list(map(int,input().split())) for _ in range(4)]
# print(f'({Max(image)[0]},{Max(image)[1]})')


# 19.5

# # 19.5-2. 안정적인 세포 판별
#
# def isStable(arr):
#     dy = [-1,-1,-1,0,1,1,1,0]
#     dx = [-1,0,1,1,1,0,-1,-1]
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             for d in range(len(dy)):
#                 if arr[i][j]:
#                     if len(arr)>dy[d]+i>=0 and len(arr[i])>dx[d]+j>=0:
#                         if arr[dy[d]+i][dx[d]+j]:
#                             return '불안정한 상태'
#     return '안정된 상태'
#
# arr=[list(map(int,input().split())) for _ in range(5)]
# print(isStable(arr))

# # 19.5-3. 핸드폰 비밀번호 순서
#
# def cell(arr,num):
#     for n in range(len(num)):
#         i=(num[n]-1)//4
#         j=(num[n]-1)%4
#         arr[i][j]=n+1
#
#     return arr
#
# arr=[[0]*4 for _ in range(4)]
# num=list(map(int,input().split()))
# arr= cell(arr,num)
# for i in range(len(arr)):
#     print(*arr[i])

# #19.5-4. 가로세로 색칠하기
#
# def paint(arr,I):
#     I[1]=int(I[1])
#     for i in range(len(arr)):
#         if I[0]== 'G':
#             arr[I[1]][i]=1
#         else:
#             arr[i][I[1]]=1
#     return arr
#
# arr=[[0]*4 for _ in range(4)]
# for _ in range(3):
#     I=input().split()
#     arr=paint(arr,I)
# for i in range(len(arr)):
#     print(*arr[i])









#
#
#
# # anagram
# def Ana(arr,arr1):
#     becket1=[0]*200
#     becket2=[0]*200
#     for i in range(len(arr)):
#         becket1[ord(arr[i])]+=1
#     for i in range(len(arr1)):
#         becket2[ord(arr1[i])] += 1
#     if becket1==becket2:
#         return '일치'
#     return '불일치'
#
# arr=input()
# arr1=input()
# print(Ana(arr,arr1))

### 강제 아나그램 만들기
# def Ana(arr,arr1):
#     becket1=[0]*200
#     becket2=[0]*200
#     cnt=0
#     for i in range(len(arr)):
#         becket1[ord(arr[i])]+=1
#     for i in range(len(arr1)):
#         becket2[ord(arr1[i])] += 1
#
#     for i in range(len(becket1)):
#         if becket1[i]!=becket2[i]:
#             cnt+=abs(becket1[i]-becket2[i])
#
#     return cnt
#
# arr=input()
# arr1=input()
# print(Ana(arr,arr1))








# #19.5-6 비밀 위치 찾기
#
# def Map(map1,pattern):
#     dy=[0,0,1,1]
#     dx=[0,1,1,0]
#     arr=[[0,0],[0,0]]
#     cnt=0
#     for i in range(len(map1)-1):
#         for j in range(len(map1[i])-1):
#             for d in range(len(dy)):
#                 arr[dy[d]][dx[d]]=map1[i+dy[d]][j+dx[d]]
#             if arr== pattern:
#                 cnt+=1
#
#     if cnt==0:
#         return '미발견'
#     return f'발견({cnt}개)'
#
# map1=[['A','B','G','K'],['T','T','A','B'],['A','C','C','D']]
# pattern=[list(input()) for _ in range(2)]
# print(Map(map1,pattern))


# #19.5-7 마스킹하고 난뒤
#
# def bitMax(map1,bit):
#     dy=[]
#     dx=[]
#     max=0
#     ddy=0
#     ddx=0
#     for i in range(len(bit)):
#         for j in range(len(bit[i])):
#             if bit[i][j]:
#                 dy=dy+[i]
#                 dx=dx+[j]
#
#     for i in range(len(map1)-len(bit)+1):
#         for j in range(len(map1[i])-len(bit[0])+1):
#             sum1=0
#             for d in range(len(dy)):
#                 sum1+=map1[i+dy[d]][j+dx[d]]
#             if sum1>max:
#                 max=sum1
#                 ddy=i
#                 ddx=j
#     return f'({ddy},{ddx})'
#
# map1=[[3,5,1],[3,8,1],[1,1,5]]
# bit=[list(map(int,input().split())) for _ in range(2)]
# print(bitMax(map1,bit))

#========================================================20============================================================

# #20-1
#
# def bbq(n):
#     if n==4:
#         return
#     bbq(n+1)
# bbq(0)


# # ## 20-2
#
# def CD(num):
#     if num==0:
#         print(num,end=' ')
#         return
#     print(num, end=' ')
#     CD(num-1)
#     print(num,end=' ')
#
# N= int(input())
# CD(N)


# #20-3. 마이클잭슨 무브먼트
# ar=list(map(int, input().split()))
# i=0
# def move(ar,i):
#     if i== len(ar)-1:
#         print(ar[i],end=' ')
#         return
#     print(ar[i], end=' ')
#     move(ar, i+1)
#     print(ar[i],end=' ')
# move(ar,i)



#20-4. 두칸씩 점프하기

# def two(num,i):
#     if i==0:
#         print(num, end=' ')
#         return
#     two(num+2,i-1)
#     print(num, end=' ')
#
# num=int(input())
# two(num,3)

# #20-5. 다섯글자 순차/역순으로 출력
# def Sort(st,i):
#     if i==len(st)-1:
#         print(st[i])
#         print(st[i], end='')
#         return
#     print(st[i],end='')
#     Sort(st,i+1)
#     print(st[i],end='')
#
# st=input()
# Sort(st,0)

# #20-6. a, b 재귀호출
#
# def abc(a,b):
#     if a==b:
#         print(b,end=' ')
#         return
#     print(a, end=' ')
#     abc(a+1,b)
#     print(a, end=' ')
#
# a,b =map(int,input().split())
# abc(a,b)


# #20-7. 재귀 부메랑
#
# def Move(ar,i):
#     if i==0:
#         print(ar[i], end=' ')
#         return
#     print(ar[i], end=' ')
#     Move(ar,i-1)
#     print(ar[i], end=' ')
#
# ar=[3,7,4,1,9,4,6,2]
# i=int(input())
# Move(ar,i)


# #20-8. 없어질때까지 나눠먹기
#
# def abc(num):
#     if num==0:
#         return
#     abc(num//2)
#     print(num, end=' ')
#
# num=int(input())
# abc(num)


# # #20.5-1. BBQ 갔다오기
# def BBQ(i):
#     if i==0:
#         return
#     BBQ(i-1)
# BBQ(3)

# # #20.5-2. 앞으로 돌진하는 계단
# #
# def abc(st,i):
#     if i==len(st)-1:
#         print(st[i:])
#         return
#     abc(st,i+1)
#     print(st[i:])
# st=input()
# abc(st,0)

# #20.5-3 절반 나누기
#
# def eq(st):
#     if st[0:len(st)//2]==st[len(st)//2: ]:
#         return '동일한문장'
#     return '다른문장'
# st=input()
# print(eq(st))


# # #20.5-4
#
# def bit(arr1,arr2):
#     for i in range(len(arr1)):
#         for j in range(len(arr1)):
#             if arr1[i][j]==1 and arr2[i][j]==1:
#                 return '걸리다'
#     return '걸리지않는다'
# arr1=[list(map(int,input().split())) for _ in range(4)]
# Pass=input()
# arr2=[list(map(int,input().split())) for _ in range(4)]
# print(bit(arr1,arr2))

#20.5-5 일곱계단 만들기

# def Asc(st,i):
#     if st+i>ord('Z'):
#         st-=ord('Z')-ord('A')+1
#     elif st+i<ord('A'):
#         st+= ord('Z')-ord('A')+1
#     if i==3:
#         print(chr(st+i),end='')
#         return
#     print(chr(st+i),end='')
#     Asc(st,i+1)
# st=ord(input())
# Asc(st,-3)


# #20.5-6 성쌓기
#
# ar=list(map(int,input().split()))
# for i in range(3, len(ar)):
#     print(*ar[0:i+1])

# #20.5-7 늘어나는 글자
#
# def PPrint(st):
#     if len(st)==1:
#         print(st)
#         return
#     PPrint(st[:-1])
#     print(st)
#
# st=input()
# PPrint(st)

# #20.5-8 두배열 머지(Merge)하기
#
#
# def merge(ar1,ar2):
#     result=[]
#     s1=s2=0
#     while(1):
#         if ar1[s1]<=ar2[s2]:
#             result.append(ar1[s1])
#             s1+=1
#         else:
#             result.append(ar2[s2])
#             s2 += 1
#         if s1==len(ar1):
#             result.extend((ar2[s2:]))
#             return result
#         if s2==len(ar1):
#             result.extend((ar1[s1:]))
#             return result
#
# ar1=list(map(int,input().split()))
# ar2=list(map(int,input().split()))
# print(*merge(ar1,ar2))


# #20.5-9 원하는 패턴의 크기 적용
#
# def Max(arr,N,M):
#     max1=0
#
#     for i in range(len(arr)-N+1):
#         sum1 = 0
#         for n1 in range(N):
#             for n2 in range(M):
#                 sum1+=arr[i+n1][n2]
#
#         for j in range(len(arr[i])-M+1):
#             if sum1>max1:
#                 max1=sum1
#                 d= (i,j)
#
#             if j==len(arr[i])-M:
#                 break
#             for n in range(N):
#                 sum1+=arr[i+n][j+M]
#                 sum1-=arr[i+n][j]
#     return d
#
# arr=[[3,5,4,2,5],[3,3,3,2,1],[3,2,6,7,8],[9,1,1,3,2]]
# N,M=map(int,input().split())
# print(f'({Max(arr,N,M)[0]},{Max(arr,N,M)[1]})')


#========================================== 21 ======================================

#21-1 재귀호출이 3개일때

# def abc(level):
#     if level==2:
#         return
#
#     for i in range(3):
#         abc(level+1)


#21-2. 로그인 처리하기



# #21-3. Level과 Branch
#
# def abc(level):
#     if level==N:
#         return
#     for i in range(M):
#         abc(level+1)
# N=int(input())
# M=int(input())
# abc(0)


#21-4. 입력받은 Level까지 재귀함수 동작

# def abc(level):
#
#     if level==N:
#         print(level, end='')
#         return
#     print(level, end='')
#
#     for i in range(2):
#         abc(level+1)
#
#
# N=int(input())
# abc(0)

# #21-6. 재귀는 몇번
#
# def abc(level):
#     global cnt
#     cnt += 1
#     if level==N:
#         return
#     for i in range(branch):
#         abc(level+1)
#
#
# cnt=0
# branch,N=map(int,input().split())
# abc(0)
# print(cnt)

# #21-7. 글자수만큼 손가락 접기
#
# def abc(st):
#     if len(st)==1:
#         print(len(st),end=' ')
#         return
#     print(len(st),end=' ')
#     abc(st[:-1])
#     print(len(st),end=' ')
#
# st=input()
# abc(st)


# #21-8. 생일선물 마우스
#
# def Move(level,dy,dx):
#
#         if ar[level]=='up':
#             dy-=1
#         elif ar[level]=='down':
#             dy+=1
#         elif ar[level]=='left':
#             dx-=1
#         elif ar[level]=='right':
#             dx+=1
#         elif ar[level]=='click':
#             print(dy,',',dx, sep='')
#         if level==N-1:
#             return
#         Move(level+1,dy, dx)
#         return
#
# N=int(input())
# ar=[input() for _ in range(N)]
# Move(0,5,5)

# # #21.5-1.너에게 가려면
# #
# def abc(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]=='A':
#                 i_a,j_a=i, j
#             if arr[i][j]=='B':
#                 i_b, j_b=i,j
#     return(abs(i_a-i_b)+abs(j_a-j_b))
#
# arr=[input() for _ in range(4)]
# print(abc(arr))


# #21.5-2. 세로줄의 합과 해당 인덱스값 구하기
#
# def InSum(arr):
#     ar_sum1=[]
#     for i in range(4):
#         sum1=0
#         for j in range(3):
#             sum1+=arr[j][i]
#         ar_sum1.append(sum1)
#     return ar_sum1[index]
# arr=[[3,4,1,5],[3,4,1,3],[5,2,3,6]]
# index=int(input())
# print(InSum(arr))

# #21.5-3. 문자 양옆으로 #넣기
#
# def abc(st,s1,s2):
#     for i in range(len(st)):
#         if st[i]==s1 or st[i]==s2:
#             if i-1>=0:
#                 st[i-1]='#'
#             if i+1<len(st):
#                 st[i+1]='#'
#     return st
# st=list(input())
# s1,s2=input().split()
# print(*abc(st,s1,s2),sep='')


# # #21.5-4. 중력문제
# # #
# def Gr(arr):
#     for i in range(len(arr[0])):
#         for j in range(len(arr)-1,-1,-1):
#             if arr[j][i]!='_':
#                 while j<3 and arr[j+1][i]=='_':
#                     arr[j][i],arr[j+1][i]= arr[j+1][i],arr[j][i]
#                     j+=1
#     return arr
# arr=[list(input()) for _ in range(4)]
# for i in range(len(arr)):
#     print(*Gr(arr)[i],sep='')

#--------------------------------
# def abc(s,e):
#
#     if s<=e:
#         arr = [['0'] * (e - s + 1) for _ in range(9)]
#         for i in range(9):
#             for j in range(e-s+1):
#                 arr[i][j]=f'{j+s} * {i+1} = {(j+s)*(i+1)}'
#     else:
#         arr = [['0'] * (s-e+1) for _ in range(9)]
#         for i in range(9):
#             for j in range(s-e+1):
#                 arr[i][j]=f'{s-j} * {i+1} = {(i+1)*(s-j)}'
#     return arr
#
# TC=int(input())
# for t in range(1,TC+1):
#     s,e=map(int,input().split())
#     print(f'#{t}')
#     for i in range(9):
#         print(*abc(s,e)[i],sep='   ')

#------------------------------


# #21.5-5 counting 후 정렬하기
#
# def Counting(vect):
#     bucket=[0]*10
#     for i in range(len(vect)):
#         bucket[vect[i]]+=1
#     for i in range(len(bucket)):
#         if bucket[i]>0:
#             print(*[i]*bucket[i],end=' ')
#     return
# vect=[1,9,3,1,0,1,0,7]
# Counting(vect)

# #21.5-6 범위의 숫자 #으로 바꾸기
#
# def abc(arr,a,b):
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if b>=arr[i][j]>=a:
#                 arr[i][j]='#'
#     return arr
# arr=[[1,5,3],[4,5,5],[3,3,5],[4,6,2]]
# a,b=map(int,input().split())
# arr=abc(arr,a,b)
# for i in range(len(arr)):
#     print(*arr[i])

# #21.5-7 바둑이 게임
#
# def abc(arr,y,x):
#     dy=[-1,0,1,0]
#     dx=[0,1,0,-1]
#     arr[y][x]=1
#     cnt=0
#     for i in range(len(arr)):
#         for j in range(len(arr[i])):
#             if arr[i][j]==2:
#                 sum1=0
#                 for d in range(4):
#                     if 6>=i+dy[d]>=0 and 6>=j+dx[d]>=0:
#                         if arr[i+dy[d]][j+dx[d]]==1:
#                             sum1+=1
#                 if sum1==4:
#                     cnt+=1
#     return cnt
# arr=[[0,0,0,0,0,0,0],[0,0,1,0,1,0,0],[0,1,2,0,2,1,0],[0,0,1,2,1,0,0],[0,0,2,1,0,1,0],[0,1,1,0,0,0,0],[0,0,0,0,0,0,0]]
# y,x=map(int,input().split())
# print(abc(arr,y,x))


#21.5-8 모델 위치 지시하기

# def abc(arr):
#     for i in range(len(arr)):
#         for j in range(len((arr[i]))):
#             if arr[i][j] in ['A','T','K']:
#                 y=i
#                 x=j
#                 if arr[i][j] == 'A':
#                     D=A[:]
#                     A.clear()
#                 elif arr[i][j]=='T':
#                     D=T[:]
#                     T.clear()
#                 elif arr[i][j]=='K':
#                     D=K[:]
#                     K.clear()
#                 for d in range(len(D)):
#                     if D[d]=='UP'and y>0:
#                         arr[y-1][x]=arr[y][x]
#                         arr[y][x]='_'
#                         y-=1
#                     elif D[d]=='DOWN' and y<4:
#                         arr[y+1][x]=arr[y][x]
#                         arr[y][x] = '_'
#                         y+=1
#                     elif D[d]=='RIGHT' and x<2:
#                         arr[y][x+1]=arr[y][x]
#                         arr[y][x] = '_'
#                         x+=1
#                     elif D[d]=='LEFT' and x>0:
#                         arr[y][x-1]=arr[y][x]
#                         arr[y][x] = '_'
#                         x-=1
#     return arr
#
#
# arr=[['_','_','_'],['_','_','_'],['A','T','K'],['_','_','_'],['_','_','_']]
# A=[]
# T=[]
# K=[]
# for _ in range(7):
#     st,m=input().split()
#     if st=='A':
#         A.append(m)
#     elif st=='T':
#         T.append(m)
#     else:
#         K.append(m)
# for i in range(len(arr)):
#     print(*abc(arr)[i],sep='')

#=================================== 22 =======================================

# #22.-1 경로를 출력하자
# arr=['A','B','C']
# path=['']*2
# def abc(level):
#     global path
#     if level==2:
#         print(*path,sep='')
#         return
#     for i in range(3):
#         path[level]=arr[i]
#         abc(level+1)
# abc(0)

# #22-3. 경로 이름은 BGTK
#
# arr=['B','G','T','K']
# N=int(input())
# path=['']*N
#
# def abc(level):
#     global path
#     if level==N:
#         print(*path,sep='')
#         return
#     for i in range(4):
#         path[level]=arr[i]
#         abc(level+1)
# abc(0)

# #22-4. Up & Down
# i=[input() for _ in range(5)]
# def abc(level,floor):
#
#     if level==5:
#         if floor>0:
#             print(floor)
#             return
#         else:
#             print('B',-floor+1,sep='')
#             return
#     if i[level]=='up':
#         abc(level+1,floor+1)
#     else:
#         abc(level+1,floor-1)
# abc(0,1)

# #22-5.청소당번
# n=int(input())
# path=['']*4
# def abc(level):
#     global path
#     if level==4:
#         print(*path,sep='')
#         return
#     for i in range(n):
#         path[level]=i+1
#         abc(level+1)
# abc(0)

#22-7. 몇번째 행운
# ar=['A','B','C','D']
# path=['']*3
# cnt=0
# luck=list(input())
# def abc(level):
#     global path, cnt
#     if level==3:
#         cnt+=1
#         if path==luck:
#             print(f'{cnt}번째')
#             return
#         else:
#             return
#     for i in range(4):
#         path[level]=ar[i]
#         abc(level+1)
# abc(0)

#22-8. 3차 배열에서 MAX MIN 찾기

# arrr=[[[2,4],[1,5]],[[2,3],[3,6]],[[7,3],[1,5]]]
#
# N=int(input())
#
# def abc(N):
#     max1 = 0
#     min1 = 1000
#     for i in range(len(arrr[N])):
#         for j in range(len(arrr[N][i])):
#             if arrr[N][i][j]>max1:
#                 max1=arrr[N][i][j]
#             if arrr[N][i][j]<min1:
#                 min1 = arrr[N][i][j]
#     print(f'MAX={max1}')
#     print(f'MIN={min1}')
#     return
# abc(N)

# #22-9. 암호 해독하기
# ar=[['Jason'],['Dr.tom'],['EXEXI'],['GK12P'],['POW']]
# st=input()
# def abc(level):
#     if level==len(ar)-1:
#         if ar[level][0]==st:
#             print('암호해제')
#             return
#         else:
#             print('암호틀림')
#             return
#     if ar[level][0]==st:
#         print('암호해제')
#         return
#     else:
#         abc(level+1)
# abc(0)



































