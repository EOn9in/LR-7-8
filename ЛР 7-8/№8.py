a = input()
x = a.count('x')
w = a.count('w')
if (x or w)==0:
  print('В строке нет букв x или w')
else:
  if a.index('x') < a.index('w'):
    print('х встретился раньше w')
  else:
    print('w встретился раньше x')