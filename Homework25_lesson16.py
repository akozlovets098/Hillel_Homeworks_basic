import telebot
import requests
import os


url_auth = 'https://developers.lingvolive.com/api/v1.1/authenticate'
url_translate = 'https://developers.lingvolive.com/api/v1/Minicard'
key = os.environ.get('translate_api')


def get_auth_token(key, url_auth):
    headers_auth = {'Authorization': 'Basic ' + key}
    auth = requests.post(url=url_auth, headers=headers_auth)
    if auth.status_code == 200:
        cur_token = auth.text
        return cur_token
    else:
        print('Error - ' + str(auth.status_code))
        return ''


def translate(cur_token, url_translate, word):
    headers_translate = {'Authorization': 'Bearer ' + cur_token}
    params_en_to_ru = {
        'text': word,
        'srcLang': 1033,
        'dstLang': 1049
    }
    req = requests.get(url_translate, headers=headers_translate, params=params_en_to_ru)
    if req.status_code != 200:
        return 'unknown'
    else:
        res = req.json()
        value = res['Translation']['Translation']
        return value


token = os.environ.get('telegram_key')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hi! I am simple translator from English to Russian. '
                                      'Please input one word you want to translate')


@bot.message_handler(regexp='.*')
def any_message(message):
    my_token = get_auth_token(key=key, url_auth=url_auth)
    bot.send_message(message.chat.id, translate(cur_token=my_token, url_translate=url_translate, word=message.text))


bot.infinity_polling()
