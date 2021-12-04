# Улучшенный калькулятор
list_for_calc = []
while True:
    number = input('Type the number\n')
    try:
        number = int(number)
    except:
        try:
            number = float(number)
        except:
            print('It is not a valid number. Please re-run the program')
            break
    list_for_calc.append(str(number))
    oper = input('Type the operator (to finish input and get the result, please type"=")\n')
    if oper not in '+-*/=':
        print('It is not a valid operator. Please re-run the program')
        break
    if oper == '=':
        print('The result of calculation is ', eval(''.join(list_for_calc)))
        break
    list_for_calc.append(oper)

