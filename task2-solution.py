str1 = input('Введи первое число: ')
str2 = input('Введи второе число: ')
operator = input('Введи операцию: ')

a = float(str1)
b = float(str2)

if operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif operator == '*':
    result = a * b
elif operator == '/':
    result = a / b
else:
    result = 'Введена неправильная операция'
    

print(result)
