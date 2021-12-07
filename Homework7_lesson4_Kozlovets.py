# шла через список (без использования метода .replace()) чтоб избежать случаев,
# когда программа заменяет часть слова, а не все слово
text = input('Please type your text\n').lower().split()
to_find = input('Which word do you want to replace?\n')
to_replace = input('Which word should it be replaced with?\n')
numb = text.count(to_find)
for i in range(len(text)):
    if text[i] == to_find:
        text[i] = to_replace
print(' '.join(text))
print(numb)