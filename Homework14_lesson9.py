# Наибольший общий делитель
def greatest_denominator(num1, num2):
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            denominator = i
            break
    return denominator

print(greatest_denominator(100, 220))