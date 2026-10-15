import sys
sys.setrecursionlimit(10**6)
#s=[int(i) for i in input().split()]
n=int(input())
pa=list(range(n))
sz = [1] * n
print(pa,sz)

def find(x, pa):
  if pa[x] == x:
    return x
  pa[x] = find(pa[x], pa)
  return pa[x]


def unite(x, y, pa, sz):
  root_x = find(x, pa)
  root_y = find(y, pa)
  if root_x == root_y:
    #return False,0
    return False
  if sz[root_x] < sz[root_y]:
    root_x, root_y = root_y, root_x
  #new_pairs = sz[root_x] * sz[root_y]
  pa[root_y] = root_x
  sz[root_x] += sz[root_y]
  #return True, new_pairs
  return True
  
def same(x, y, pa):
  return find(x, pa) == find(y, pa)

def get_size(x, pa, sz):
  return sz[find(x, pa)]


unite(4,6,pa,sz)
unite(5,3,pa,sz)
print(pa,sz)
print(same(5,3,pa))

unite(5,1,pa,sz)
print(get_size(5, pa, sz))
print(pa,sz)

unite(5,2,pa,sz)
print(pa,sz)
unite(1,0,pa,sz)
print(pa,sz)
#for i in range(n):
#  find(i)
#print(pa)
unite(6,7,pa,sz)
print(pa,sz)
unite(6,0,pa,sz)
print(pa,sz)
for i in range(n):
  find(i,pa)
unite(7,9,pa,sz)
print(pa,sz)
unite(8,1,pa,sz)
print(pa,sz)
print(find(9,pa))