from PIL import Image


def resize(image, new_width, new_height):  # если на вход подаются новые размеры (картинка может искажаться)
    im = Image.open(image)
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im.show()


def resize_by_scale(image, scale):  # если на вход подается масштаб
    im = Image.open(image)
    width, height = im.size
    new_width, new_height = round(width*scale), round(height*scale)
    im = im.resize((new_width, new_height), Image.ANTIALIAS)
    im.show()
    print(im.size)


resize('pexels-vanessa-loring-5968231.jpg', 200, 150)  # тестировала на рандомной картинке
resize_by_scale('pexels-vanessa-loring-5968231.jpg', 0.1)  # при большом масштабе (например, 5 - увеличить в 5 раз) возникает ошибка