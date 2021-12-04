# Простые числа
number = input('Please type the number\n')
number = int(number) if number.isdigit() else ('Not a number, try again')
print('Your required primes are', end=' ')
for i in range(2, number):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i, end=', ')