import random
import sqlite3
import time

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def quest(id_user):
    db = sqlite3.connect('db_local.db')
    try:
        k = db.execute('SELECT chis FROM bot_info WHERE user_id = ?', id_user).fetchone()
    except sqlite3.OperationalError:
        db.execute('''CREATE TABLE bot_info (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id, chis INTEGER)''')
        k = list()

    if k == list():
        db.execute('''''')


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
    quest(533609675)
    listen_in_chat()


def zap():
    print('слушаю')
    msg = ' '
    mas = []
    vk_session = vk_api.VkApi(
        token='d40c66d6f609a4a50b4e470b6a0f015a1d69e982f3cc16addbb946d44dfa90eba540bf2e6d20f07b25ed8')
    vk = vk_session.get_api()
    long_poll = VkBotLongPoll(vk_session, '189131918')
    # r = QuestOne()
    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.obj)
            if len(str(event.obj.get('message').get('peer_id'))) > 9:
                if event.obj.get('message').get('text').lower() in ['ммм', 'хентай', 'аниме', 'жопа', 'грудь']:
                    msg = 'Хентай'

                elif event.obj.get('message').get('text').lower() in ['...', 'заткнись', 'сука', 'пизда', 'хех']:
                    msg = '*ушёл*'
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=msg)
                    time.sleep(2)
                    msg = '*пришёл*'
                elif 'актив' in event.obj.get('message').get(
                        'text').lower() and '[club189131918|@my_gk]' in event.obj.get('message').get('text').lower():
                    for _ in range(10):
                        vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                         random_id=random.randint(1, 9489979897999),
                                         message='общение')
                else:
                    msg = ''

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
