# ライブラリ置き場: https://github.com/furupon2008/atcoder-library (を使用)
from heapq import heappop, heapify, heappush
#n=int(input())
n,M=map(int,input().split())
#k=list(map(int,input().split()))
#s=input()
#print(n,M)
c=[0]*(n+1)
to=[[] for _ in range(n+1)]
for _ in range(M):
  a,b=map(int,input().split())
  #print(ai,bi)
  c[a]+=1
  to[a].append(b)
#print(to)
hq=[]
rm=[]
for i in range(1,n+1):
  heappush(hq,(-c[i],i)) 
#print(hq)
for i in range(1,n+1):
  #print(to[i])
  heappush(rm,(-c[i],i))
  for j in to[i]:
    #print(j)
    c[i]-=1
    heappush(rm,(-c[j],j))
    c[j]+=1
    heappush(hq,(-c[j],j))
  heappush(hq,(-c[i],i))
  while hq and rm and hq[0]==rm[0]:
    heappop(hq)
    heappop(rm)
  print(hq[0][1])  
  heappush(rm,(-c[i],i))
  for j in to[i]:
    #print(j)
    c[i]+=1
    heappush(rm,(-c[j],j))
    c[j]-=1
    heappush(hq,(-c[j],j))
  heappush(hq,(-c[i],i))
  #print(hq,rm)  
  
  
