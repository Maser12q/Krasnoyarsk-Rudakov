import requests


def save_image_with_url(url):
    try:
        img = requests.get(url)  # адрес картинки
    except ValueError:
        print('String dummles!')
    out = open("img.jpg", "wb")  # где img.jpg твоя картинка
    out.write(img.content)
    out.close()
