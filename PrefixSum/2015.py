# -*- coding: cp949 -*- 

import sys

N,K=map(int,input().split())

A=list(map(int,input().split()))
cnt=dict()#map 자료구조를 특성 이용
sumv=0
ans=0
cnt[0]=1

for i in A:
    sumv+=i
    if cnt.get(sumv-K) !=None:#cnt에 sumv-K를 만족하는 키가 있을때  sumv-들어가있는키=K
        ans+=cnt.get(sumv-K)
    if cnt.get(sumv): #키가 있을때
        cnt[sumv]+=1
    else: #키가 없을때
        cnt[sumv]=1
    
print(ans)