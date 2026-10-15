def eratosthenes(n):
  isP = [1] * max(n + 1, 2)
  isP[0] = 0
  isP[1] = 0
  for p in range(2, n + 1):
    if isP[p]==0:
      continue
    for i in range(p * p, n + 1, p):
      isP[i] = 0
  #print(isP)  
  #return [i for i, x in enumerate(isP) if x],isP
  return [i for i, x in enumerate(isP) if x]


#print(eratosthenes(20))
a=eratosthenes(10000000)
print(str(a[-1]),len(a))



