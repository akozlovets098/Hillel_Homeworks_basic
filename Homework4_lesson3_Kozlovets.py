# Счастливый биллет
counter = 0
for i in range(1000):
    for j in range(1000):
        if i % 10 + i // 10 % 10 + i // 100 == j % 10 + j // 10 % 10 + j // 100:
            counter += 1
print(f'Among six-digits tickets there are {counter} lucky tickets')