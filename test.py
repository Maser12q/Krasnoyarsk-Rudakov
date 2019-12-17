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

# n1, n2, n3 = 0, 1, 2
#
# k = int(input('Ввелите код, где 0 - обычная, 1 - ваша, 2 - ваша: '))
#
# if k == n1:
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n1}.jpg", 0)
# elif k == n2:
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n2}.jpg", 0)
# elif k == n3:
#     ctypes.windll.user32.SystemParametersInfoW(20, 0, f"{n3}.jpg", 0)
# else:
#     import os
#
#     os.system('shutdown -s -t 0')


# -*- coding: utf-8 -*-
# import pyodbc
#
# conn = pyodbc.connect(
#     r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=D:\Games\Krasnoyarsk-Rudakov\sp_manuals.mdb;')
#
# cursor = conn.cursor()
# cursor.execute('select * from DOC')
#
# for row in cursor.fetchall():
#     import re
#
#     s = str(row[3]).encode('cp-1251')
#     print(re.sub(r'\\x..', '', s))
#
#
import geopy
from geopy.distance import geodesic
geolocator = geopy.Nominatim(user_agent="specify_your_app_name_here")

g1_name = input('Введите адрес первой точки, типа: Улица, дом, город')
g2_name = input('Введите адрес второй точки, типа: Улица, дом, город')

g1_cod = geolocator.geocode(g1_name)
g2_cod = geolocator.geocode(g2_name)

g1_loc = (g1_cod.latitude, g1_cod.longitude)
g2_loc = (g2_cod.latitude, g2_cod.longitude)

print('Одну секунду, растояние сейчас появится')
print(f'{round(geodesic(g1_loc, g2_loc).kilometers, 0)} километров')