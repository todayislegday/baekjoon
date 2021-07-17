import sys
import heapq

mx=[0,0,1,-1]
my=[1,-1,0,0]


N,K=map(int,input().split()) #보드 크기,바이러스

board=[]
visted=[[0 for i in range(N)] for j in range(N)]#방문안함 # 방문
count=N
while count>0:
    count-=1
    board.append(list(map(int,input().split())))


S,X,Y=map(int,input().split())

heap=[]
for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            heap.append((0,board[i][j],i,j)) #시간,바이러스,행,열
            visted[i][j]=board[i][j]

heapq.heapify(heap)

while heap:
    pt,pv,px,py=heapq.heappop(heap)

    for i in range(4):
        nx=px+mx[i]
        ny=py+my[i]

        if pt+1<=S and nx>=0 and ny>=0 and nx<N and ny<N and visted[nx][ny] == 0:
            visted[nx][ny]=visted[px][py]
            heapq.heappush(heap,(pt+1,visted[nx][ny],nx,ny))

print(visted[X-1][Y-1])
    