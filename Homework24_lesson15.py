import requests as r


def custom_request():
    method = input('Type the action you want to perform (available actions: get, head, put, post, delete)\n').lower()
    adress = input('Type the internet adress you want to send your request to\n')
    request_body = ''
    if method in ('put', 'post'):
        request_body = input('Type the request body\n')
    available_methods = {'get': r.get(adress),
                         'head': r.head(adress),
                         'put': r.put(adress, request_body),
                         'post': r.post(adress, request_body),
                         'delete': r.delete(adress)}
    available_methods[method]
    result = r.get(adress) # на экран вывожу что в итоге находится по указанному адресу
    print(result.text)


custom_request()