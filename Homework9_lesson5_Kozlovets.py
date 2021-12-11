# Повторяющиеся элементы
# проверку на то, что введен один символ не делала - то есть проверяю не обязательно по одному символу, там может
# быть их последовательность
symbols = []
print('Please type below your symbols (one at a time). Once you want to stop typing, press "="')
while True:
    symbol = input()
    if symbol == '=':
        break
    symbols.append(symbol)
if len(symbols) == len(set(symbols)):
    print('There are no repeated symbols')
for i in range(1, len(symbols)):
    if symbols[i] in symbols[:i]:
        print(f'Your first repeated symbol is "{symbols[i]}"')
        break