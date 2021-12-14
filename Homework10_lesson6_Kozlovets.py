# Конвертор
def convert(number, scale):
    convert_base = {'sm': 100, 'ft': 3.2808, 'in': 39.370, 'fath': 0.468691}
    return round(number * convert_base[scale], 2)


numb = 24
sc = 'in'
print(f'{numb} m is equal to {convert(numb, sc)} {sc}')
