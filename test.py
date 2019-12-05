import requests


def save_image_with_url(url):
    out = open("img.jpg", "wb")  # где img.jpg твоя картинка
    try:
        img = requests.get(url)  # адрес картинки
        out = open("img.jpg", "wb")  # где img.jpg твоя картинка
        out.write(img.content)
    except ValueError:
        print('String dummles!')
    finally:
        out.close()


save_image_with_url('https://sun9-61.userapi.com/c850424/v850424769/14c42a/TClmxFEvnKY.jpg')
