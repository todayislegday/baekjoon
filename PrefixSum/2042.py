import sys


def update(i,num):
    while True:
        if i>N:break        
        tree[i] +=num
        i += (i & -i)

def sum(i):
    ans=0
    while True:
        if i<=0:break
        ans+=tree[i]
        i -= (i & -i)
    return ans

N,M,K=map(int,input().split())

A=[0 for i in range(N+1)]
tree=[0 for i in range(N+1)]

for i in range(1,N+1):
    A[i]=int(sys.stdin.readline())
    update(i,A[i])

for i in range(M+K):#Tree 상태 다음에 그대로 사용
    a,b,c=map(int,sys.stdin.readline().split())
    if a==1:
        diff=c-A[b]
        A[b]=c#같은곳을 한번더 바꿧을때 차이에 대해서 구하기 위해
        update(b,diff)
    else:
        print(sum(c)-sum(b-1))



