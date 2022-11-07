a = input()
if a[:3]=='abc':
  a = 'www' + a[3:]
else:
  a = a + 'zzz'
print(a)