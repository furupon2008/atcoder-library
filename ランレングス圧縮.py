s=input()
print(s)
n=len(s)
d=[[s[0],0]]
#print(d)
for c in s:
  #print(c)
  if c==d[-1][0]:
    d[-1][1]+=1
  else:
    d.append([c,1])
print(d)