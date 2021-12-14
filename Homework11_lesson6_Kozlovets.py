# Применение конвертора
def convert(someset):
    convert_base = {'sm': 100, 'ft': 3.2808, 'in': 39.370, 'fath': 0.468691}
    return round(someset[0] * convert_base[someset[1]], 2)


def checklen(someset):
    return someset[0] >= 1


test_list = [(1, 'sm'), (2, 'ft'), (0.3, 'fath'), (4, 'in'), (0.5, 'sm')]
print(list(map(convert, filter(checklen, test_list))))

# или (о таком узнала когда уже сдала домашку)):
# print(list(map(convert, filter(lambda x: x[0] >= 1, test_list))))
