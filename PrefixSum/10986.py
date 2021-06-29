# -*- coding: cp949 -*- 

import sys

N,K=map(int,input().split())

A=list(map(int,input().split()))
cnt=dict()

cnt[0]=1
sumv=0
ans=0

for i in A:
    sumv+=i

    if sumv%K in cnt:
        ans+=cnt[sumv%K]
    
    if sumv%K in cnt:
        cnt[sumv%K]+=1
    else:
        cnt[sumv%K]=1

print(ans)