#Ввід чисел
a = float(input('Enter first number:'))
b = float(input('Enter second number:'))

#Результати обчислень
sum = a+b
subtraction = a-b
multiply = a*b

print(sum)
print(subtraction)
print(multiply)

#Не можливо ділити на 0
if b != 0:
    division = a/b
    print(division)
#Перевірка чи є число парним
    if division % 2 == 0:
     print('The division result is even.')
    else:
     print('The division result is odd.')
else:
    print('Division cannot be made')


#Перевірка чи є число парним
if sum % 2 == 0:
    print('The sum result is even.')
else:
    print('The sum result is odd.')

if subtraction % 2 == 0:
    print('The substraction result is even.')
else:
    print('The substraction result is odd.')

if multiply % 2 == 0:
    print('The multiply result is even.')
else:
    print('The multiply result is odd.')