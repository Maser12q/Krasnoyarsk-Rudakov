import random
import time

import pymorphy2
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def k_s_b(user_msg):
    morph = pymorphy2.MorphAnalyzer()
    otv_ploh = False
    otv_hor = False

    if "плох" in user_msg or \
            "ужасн" in user_msg or \
            "отвратитель" in user_msg:
        return "Ничего, скоро всё наладится"

    if "хорош" in user_msg or \
            "отлично" in user_msg or \
            "замечатель" in user_msg:
        return "Отлично, у меня тоже всё хорошо :)"

    if 'устал' in user_msg or 'заебалс' in user_msg:
        return 'отдохните, выпейте кофе, посмотрите сериал'

    if 'сдохнуть' in user_msg or 'умереть' in user_msg or 'хочу' in user_msg:
        return 'успокойтесь, послушайте музыку, поиграйте, поговорите с важными для вас людьми, ' \
               'посмотрите на профиль краша в ВК'


# def quest(vk, id_user, chat_id, msg):
#     print('*' * 40)

# db = sqlite3.connect('db_local.db')
# c = db.cursor()
# try:
#     k = db.execute(f'SELECT chis FROM bot_info WHERE user_id = {id_user}').fetchall()
# except sqlite3.OperationalError:
#     c.execute('''CREATE TABLE bot_info (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id, chis INTEGER)''')
#     k = list()
#
# print(k)
# if k == list():
#     c.execute(f'INSERT INTO bot_info VALUES(NULL, {id_user}, 2)')

# else:
# if k[0][0] > 4:
# c.execute(f'UPDATE bot_info SET chis = 2 WHERE user_id = {id_user}')
# vk.messages.send(chat_id=chat_id,
#                  random_id=random.randint(1, 9489979897999),
#                  message=f'все заново')
# vk.messages.send(chat_id=chat_id,
#                  random_id=random.randint(1, 9489979897999),
#                  message=k_s_b(msg))
# else:
# c.execute(f'UPDATE bot_info SET chis = chis + 1 WHERE user_id = {id_user}')
# vk.messages.send(chat_id=chat_id,
#                  random_id=random.randint(1, 9489979897999),
#                  message=k_s_b(msg))

# db.commit()


def listen_in_chat():
    s = input()
    if s.lower() == 'жека':
        msg_for_chat(3)
    elif s.lower() == 'тест':
        msg_for_chat(1)
    elif s.lower() in ['лиза', 'гсг', 'тест2']:
        msg_for_chat(2)
    zap()


def msg_for_chat(chat):
    vk_session = vk_api.VkApi(
        token='d40c66d6f609a4a50b4e470b6a0f015a1d69e982f3cc16addbb946d44dfa90eba540bf2e6d20f07b25ed8')
    vk = vk_session.get_api()
    vk.messages.send(chat_id=chat,
                     random_id=random.randint(1, 9489979897999),
                     message='Ку, инопланетяне! Давайте говорить\n\n\nНу гооо')


def main():
    listen_in_chat()


def zap():
    print('слушаю')
    slov = {1: True, 2: True, 3: True, 4: True}
    msg = ''
    mas = []
    vk_session = vk_api.VkApi(
        token='d40c66d6f609a4a50b4e470b6a0f015a1d69e982f3cc16addbb946d44dfa90eba540bf2e6d20f07b25ed8')
    vk = vk_session.get_api()
    long_poll = VkBotLongPoll(vk_session, '189131918')

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.obj)

            if len(str(event.obj.get('message').get('peer_id'))) > 9:
                if slov.get(event.obj.get('message').get('peer_id') - 2000000000):
                    slov[event.obj.get('message').get('peer_id') - 2000000000] = False
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message='Ку, как ваше настроение?')
                if event.obj.get('message').get('text').lower() in ['хентай', 'аниме', 'жопа', 'грудь']:
                    msg = 'Хентай - топ!'
                elif event.obj.get('message').get('text').lower() in ['ммм', '...']:
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message='Что?')

                elif event.obj.get('message').get('text').lower() in ['заткнись']:
                    msg = '*ушёл*'
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=msg)
                    time.sleep(2)
                    msg = '*пришёл*'
                elif 'спок' in event.obj.get('message').get('text').lower() and 'ноч' in event.obj.get('message').get(
                        'text').lower():
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=random.choice(['Спокойной ночи!', 'Приятных снов', 'Доброй ночи)']))

                elif 'спок' in event.obj.get('message').get('text').lower() and 'ноч' in event.obj.get('message').get(
                        'text').lower():
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=random.choice(['Ку!', 'Привет', 'Здравствуй)']))

                elif 'актив' in event.obj.get('message').get(
                        'text').lower() and 'my_gk]' in event.obj.get('message').get('text').lower():
                    for _ in range(25):
                        vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                         random_id=random.randint(1, 9489979897999),
                                         message='общение')


                else:
                    try:
                        vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                         random_id=random.randint(1, 9489979897999),
                                         message=k_s_b(event.obj.get('message').get('text').lower()))
                    except vk_api.exceptions.ApiError:
                        pass
                try:
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=msg)
                except vk_api.exceptions.ApiError:
                    pass

            else:
                if event.obj.get('message').get('text').lower() in ['ммм', 'хентай', 'аниме', 'жопа', 'грудь']:
                    msg = 'Хентай'
                elif event.obj.get('message').get('text').lower() in ['...', 'заткнись', 'сука', 'пизда', 'хех']:
                    msg = '*ушёл*'
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=msg)
                    time.sleep(10)
                    msg = '*пришёл*'
                else:
                    msg = ''

                try:
                    vk.messages.send(user_id=event.obj.get('message').get('from_id'),
                                     random_id=random.randint(1, 9489979897999),
                                     message=msg)
                except vk_api.exceptions.ApiError:
                    pass


if __name__ == '__main__':
    main()
