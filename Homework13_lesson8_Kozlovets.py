import datetime, string


def decorator_calc_time(function):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        function(*args, **kwargs)
        end_time = datetime.datetime.now()
        print('Time for function execution:', end_time - start_time)
    return wrapper


def decorator_print_args(function): # отображаю входящие аргументы функции. или нужно таки параметры?
    # если параметры, можно попробовать распаковать аргументы и к каждому применить .__name__, но я пока так не игралась :)
    def wrapper(*args, **kwargs):
        if len(args) + len(kwargs) > 0:
            print(f'Arguments of {function.__name__} function are:', *args, *kwargs, sep='\n - ')
        else:
            print(f'{function.__name__} function has no arguments')
    return wrapper


@decorator_calc_time
@decorator_print_args
def vigenere_cipher(text, keyword):
    text_upd = ''
    alphabet = string.ascii_lowercase
    keyphrase = keyword * (len(text) // len(keyword)) + keyword[:len(text) % len(keyword)]
    for text_letter, key_letter in zip(list(text.lower()), list(keyphrase.lower())):
        if text_letter in alphabet:
            text_upd += alphabet[(alphabet.index(text_letter) + alphabet.index(key_letter)) % len(alphabet)]
        else:
            text_upd += text_letter
    return text_upd


@decorator_calc_time
@decorator_print_args
def lucky_ticket():
    counter = 0
    for i in range(1000):
        for j in range(1000):
            if i % 10 + i // 10 % 10 + i // 100 == j % 10 + j // 10 % 10 + j // 100:
                counter += 1
    print(f'Among six-digits tickets there are {counter} lucky tickets')


@decorator_calc_time
@decorator_print_args
def convert(someset):
    convert_base = {'sm': 100, 'ft': 3.2808, 'in': 39.370, 'fath': 0.468691}
    return round(someset[0] * convert_base[someset[1]], 2)


vigenere_cipher('some text to cipher', 'elephant')
print() # чисто для красоты отображения
lucky_ticket()
print()
convert([(1, 'sm'), (2, 'ft'), (0.3, 'fath'), (4, 'in'), (0.5, 'sm')])
