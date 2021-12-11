# Проверка номера телефона
# Не нашла способ сделать один шаблон, чтоб не позволить поставить, например, только открывающуюся скобку и не
# закрыть ее - поэтому скобки фиксировала четко. Что касается разделения групп цифр дефисами, то я не знаю правил
# такого деления, поэтому программа позволяет пользователю разделить хоть каждую цифру
import re

numb_to_check = input('Type a phone number\n')
pattern1 = r'\+?\d{3}(\-?\d){9}'
pattern2 = r'\+?\d{2}\(\d{3}\)(\-?\d){7}'
pattern3 = r'\+?\(\d{3}\)(\-?\d){9}'
pattern4 = r'\d(\-?\d){9}'
pattern5 = r'\(\d{3}\)(\-?\d){7}'

pattern = bool(re.fullmatch(pattern1, numb_to_check)) or bool(re.fullmatch(pattern2, numb_to_check)) or \
          bool(re.fullmatch(pattern3, numb_to_check)) or bool(re.fullmatch(pattern4, numb_to_check)) or \
          bool(re.fullmatch(pattern5, numb_to_check))
print('It is a correct number' if pattern == True else 'Wrong number')
