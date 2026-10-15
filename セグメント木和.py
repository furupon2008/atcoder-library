n,Q=map(int,input().split())
#print(n,k,t)

s=list(map(int,input().split()))
#print(d)
n2=1
while n2<n:
  n2*=2
#print(n2)
s2=[0]*(2*n2)
for i in range(n):
  s2[n2+i]=s[i]
#print(s2)
for i in range(n2-1,0,-1):
  s2[i]=s2[2*i]+s2[2*i+1]
#print(s2)

def fn1(l,r):
  l=n2+l-1
  r=n2+r
  ret=0
  while l<r:
    if l%2==1:
      ret+=s2[l]
      l+=1
    if r%2==1:
      r-=1
      ret+=s2[r]
    l//=2
    r//=2
  return ret
  
def fn2(x,v):
  x=n2+x-1
  s2[x]=v
  while x>1:
    x//=2
    s2[x]=s2[2*x]+s2[2*x+1]
  

for _ in range(Q):
  q,x,y=map(int,input().split())
  #print(q,x,y)
  if q==1:
    z=fn1(x,y)
    print(z)
  else:
    fn2(x,y)
  

