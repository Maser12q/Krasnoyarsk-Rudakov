# import requests
#
#
# def save_image_with_url(url):
#     out = open("img.jpg", "wb")  # где img.jpg твоя картинка
#     try:
#         img = requests.get(url)  # адрес картинки
#         out = open("img.jpg", "wb")  # где img.jpg твоя картинка
#         out.write(img.content)
#     except ValueError:
#         print('String dummles!')
#     finally:
#         out.close()
#
# # save_image_with_url('https://sun9-61.userapi.com/c850424/v850424769/14c42a/TClmxFEvnKY.jpg')


import ctypes

n1, n2, n3 = 0, 1, 2

k = int(input('Ввелите код, где 0 - обычная, 1 - ваша, 2 - ваша: '))

if k == n1:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n1}.jpg", 0)
elif k == n2:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n2}.jpg", 0)
elif k == n3:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n3}.jpg", 0)
else:
    import os

    os.system('shutdown -s -t 0')
