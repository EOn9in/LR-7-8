s = input()
a = s.count('a')
b = s.count('b')
c = s.count('c')
if (a+b+c)!=len(s):
  print('Cтрока не состоит только из a,b,c')
else:
  print('Строка состоит из a,b,c')