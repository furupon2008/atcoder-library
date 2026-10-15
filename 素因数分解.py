st=set()

def fnp1(x):
  ret=[]
  i=2
  xx=x
  while i*i<=x:
    while xx%i==0:
      st.add(i)
      ret.append(i)
      xx//=i
    i+=1
  if xx!=1:
    st.add(xx)
    ret.append(xx)
  return ret


x=int(input())
print(fnp1(x))
print(st)