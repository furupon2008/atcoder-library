s=input()
i = 0
ans=[]
while i < len(s):
  char = s[i]
  i += 1
  num = 0
  while i < len(s) and s[i].isdigit():
    num = num*10+int(s[i])
    i += 1
  print(char,num)
  ans.append(char*num)
print(ans)
print("".join(ans))