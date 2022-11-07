a = list(input())
if len(a)>10:
  print(''.join(a[0:6]))
else:
  i=len(a)
  while i<12:
    a.append('o')
    i+=1
  print(''.join(a))