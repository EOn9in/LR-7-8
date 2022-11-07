a = list(input())
if len(a)==1:
  print(a[0])
elif len(a)==2:
  print(a[0],a[-1])
else:
  print(a[0],a[len(a)//2],a[-1])