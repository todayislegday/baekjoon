# -*- coding: cp949 -*- 
import sys


N,M=map(int,input().split()) #���� ���� �ΰ��Է� ����


numlist=list(map(int,input().split()))
sumlist=list()
sumv=0
sumlist.append(sumv)#0��° ���� ���Ѱ�,���� e��s�� ���ؼ� �ε��� ������ �ƴϰ� �״�� ����ϱ� ���ϰ� �ϱ�����

for i in numlist:
       sumv+=i
       sumlist.append(sumv)

for i in range(M):
      s,e=map(int,sys.stdin.readline().split())
      print(sumlist[e]-sumlist[s-1])

