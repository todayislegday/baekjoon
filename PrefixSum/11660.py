# -*- coding: cp949 -*- 

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [[0]*(n+1) for _ in range(n+1)]
s = [[0]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    a[i][1:] = list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])

# import sys

# N,M=map(int,input().split())

# A=[]
# S=[[0 for j in range(N+1)] for i in range(N+1)] 

# temp=[]
# for i in range(N+1):
#     temp.append(0)
# A.append(temp)

# for i in range(N):
#     temp=list(map(int,sys.stdin.readline().split()))
#     temp.insert(0,0)
#     A.append(temp)

# for i in range(1,N+1):
#     for j in range(1,N+1):
#         S[i][j]=S[i-1][j]+S[i][j-1]-S[i-1][j-1]+A[i][j]

# for i in range(M):
#     x1,y1,x2,y2=map(int,sys.stdin.readline().split())
#     print(S[x2][y2]-S[x2][y1-1]-S[x1-1][y2]+S[x1-1][y1-1])

