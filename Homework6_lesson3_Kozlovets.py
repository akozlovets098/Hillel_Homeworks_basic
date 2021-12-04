# Улучшенный определитель марок
def mark_by_name():
    ford = ['mondeo', 'focus', 'kuga']
    fiat = ['tipo', 'panda', '500']
    renault = ['clio', 'megan', 'duster']
    while True:
        name = input('Please type the name of car. Once you want to exit, type "exit"\n')
        if name in ford:
            print('Mark of car is Ford')
        elif name in fiat:
            print('Mark of car is Fiat')
        elif name in renault:
            print('Mark of car is Renault')
        elif name == 'exit':
            print('See you later :)')
            break
        else:
            print('Unknown name of car')
mark_by_name()