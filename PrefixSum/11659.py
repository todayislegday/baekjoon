# -*- coding: cp949 -*- 
import sys


N,M=map(int,input().split()) #공백 기준 두개입력 받음


numlist=list(map(int,input().split()))
sumlist=list()
sumv=0
sumlist.append(sumv)#0번째 까지 더한값,이후 e와s에 대해서 인덱스 개념이 아니고 그대로 사용하기 편하게 하기위해

for i in numlist:
       sumv+=i
       sumlist.append(sumv)

for i in range(M):
      s,e=map(int,sys.stdin.readline().split())
      print(sumlist[e]-sumlist[s-1])

