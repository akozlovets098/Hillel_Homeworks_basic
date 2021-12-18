import string, datetime

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


def vigenere_decipher(text, keyword):
    text_upd = ''
    alphabet = string.ascii_lowercase
    keyphrase = keyword * (len(text) // len(keyword)) + keyword[:len(text) % len(keyword)]
    for text_letter, key_letter in zip(list(text.lower()), list(keyphrase.lower())):
        if text_letter in alphabet:
            text_upd += alphabet[alphabet.index(text_letter) - alphabet.index(key_letter)]
        else:
            text_upd += text_letter
    return text_upd


def function_time(function):
    time_start = datetime.datetime.now()
    function
    time_end = datetime.datetime.now()
    return function, time_end - time_start


print(function_time(vigenere_cipher('some text to cipher', 'elephant')))
print(function_time(vigenere_decipher('wzqt trqx xd cvilpv', 'elephant')))