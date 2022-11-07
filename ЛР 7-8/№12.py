a = input()
b = (''.join([i for i in a if i.isdigit()]))
print('Количество цифр в тексте = ', len(b))