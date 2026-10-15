#n=int(input())
n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
#print(n,q,a)
#print(max(a),min(a))
#hi=max(a)-min(a)
#print(hi,lo)


def fn1(a,x):
  l=-1
  r=n
  while r-l>1:
    md=(l+r)//2
    if a[md]<=x:
      l=md
    else:
      r=md
  return (l,r)
  
def fn2(a,x):
  l=-1
  r=n
  while r-l>1:
    md=(l+r)//2
    if a[md]<x:
      l=md
    else:
      r=md
  return (l,r)
  
def fn3(x,w):
  l1,r1=fn1(a,x+w)
  l2,r2=fn2(a,x-w)
  y=l1-r2+1
  return y

#print(fn3(-1,6))

for _ in range(q):
  bi,ki=map(int,input().split())
  #print("bi,ki",bi,ki)
  hi=10**9
  lo=-1
  #print(fn3(bi,hi))
  while hi-lo>1:
    md=(hi+lo)//2
    if fn3(bi,md)<ki:
      lo=md
    else:
      hi=md
  print(hi)


 