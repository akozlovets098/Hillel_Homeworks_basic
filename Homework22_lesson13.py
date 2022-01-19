import requests, json


def weather(city):
    source_json = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=fc35cccde37a1642bad8643283894478&units=metric')
    work_dict = json.loads(source_json.text)
    print(f'City: {work_dict["name"]}')
    print(f'Temperature: {work_dict["main"]["temp"]} degrees Celsius, feels like {work_dict["main"]["feels_like"]} degrees Celsius')
    print(f'Pressure: {work_dict["main"]["pressure"]} hPa')
    print(f'Wind: {work_dict["wind"]["speed"]} m/s in {work_dict["wind"]["deg"]} degree azimuth direction')


weather('Kyiv')
print()
weather('London')
print()
weather('Paris')