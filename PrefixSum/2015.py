# -*- coding: cp949 -*- 

import sys

N,K=map(int,input().split())

A=list(map(int,input().split()))
cnt=dict()#map �ڷᱸ���� Ư�� �̿�
sumv=0
ans=0
cnt[0]=1

for i in A:
    sumv+=i
    if cnt.get(sumv-K) !=None:#cnt�� sumv-K�� �����ϴ� Ű�� ������  sumv-���ִ�Ű=K
        ans+=cnt.get(sumv-K)
    if cnt.get(sumv): #Ű�� ������
        cnt[sumv]+=1
    else: #Ű�� ������
        cnt[sumv]=1
    
print(ans)