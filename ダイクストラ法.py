import heapq
n,m=map(int,input().split())
#n=int(input())
inf=10000
dist=[inf]*n
to=[[] for _ in range(n)]
#print(to,dist)
for i in range(m):
  a,b,c=map(int,input().split())
  to[a].append([b,c])
  to[b].append([a,c])
#print(to)
q=[[0,0]]
dist[0]=0
while q:
  print(q,dist)
  d,u=heapq.heappop(q)
  if d!=dist[u]:
    continue
  #print(u,d,dist)
  for v,c in to[u]:
    #print(v)
    nd=d+c
    if nd>=dist[v]:
      continue
    dist[v]=nd
    heapq.heappush(q,[nd,v])
print(dist[n-1])
    
  
  

