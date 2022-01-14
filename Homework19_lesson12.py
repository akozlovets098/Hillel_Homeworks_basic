# Числа Фибоначчи

def fibonacci(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        f = fibonacci(n-1)
        f.append(f[-1] + f[-2])
        return f

print(fibonacci(15))