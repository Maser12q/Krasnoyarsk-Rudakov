# import random
#
# import vk
#
# session = vk.Session('d40c66d6f609a4a50b4e470b6a0f015a1d69e982f3cc16addbb946d44dfa90eba540bf2e6d20f07b25ed8')
# api = vk.API(session, v='5.103', lang='ru', timeout=10)
#
# api.messages.getLastActivity(user_id='248667120')
# # print(api.messages.send())
#
# '''4d36712eec3fab80a5987e8efcb3824f1688aedeaadc65236e74b940e9008161b4ac06457aedf9e9464e4'''
import random
import time

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


def main():
    zap()


def zap():
    msg = ' '

    vk_session = vk_api.VkApi(
        token='d40c66d6f609a4a50b4e470b6a0f015a1d69e982f3cc16addbb946d44dfa90eba540bf2e6d20f07b25ed8')
    vk = vk_session.get_api()
    long_poll = VkBotLongPoll(vk_session, '189131918')

    for event in long_poll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event.obj)
            if len(str(event.obj.get('message').get('peer_id'))) > 9:
                if event.obj.get('message').get('text').lower() in ['ммм', 'хентай', 'аниме', 'жопа', 'грудь']:
                    msg = 'Хентай - топ!'
                elif event.obj.get('message').get('text').lower() in ['...', 'заткнись', 'сука', 'пизда', 'хех']:
                    msg = '*ушёл*'
                    vk.messages.send(chat_id=event.obj.get('message').get('peer_id') - 2000000000,
                                     random_id=random.randint(1, 9489979897999),
                                     message=msg)
                    time.sleep(2)
                    msg = '*пришёл*'
                elif 'програм' in event.obj.get('message').get('text').lower() and 'сохран' in event.obj.get(
                        'message').get('text').lower():
                    owner_id = event.obj.get('message').get('attachments')[0].get('doc').get('owner_id')
                    id_doc = event.obj.get('message').get('attachments')[0].get('doc').get('id')
                    token = event.obj.get('message').get('attachments')[0].get('doc').get('access_key', '')
                    vk.docs.add(owner_id=owner_id, doc_id=id_doc, access_key=token)
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
                    msg = 'Хентай - топ!'
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


        elif event.type == VkBotEventType.MESSAGE_REPLY:
            print('Новое сообщение:')
            print('От меня для: ', end='')
            print(event.obj.peer_id)
            print('Текст:', event.obj.text)
            print()

        elif event.type == VkBotEventType.MESSAGE_TYPING_STATE:
            print('Печатает ', end='')
            print(event.obj.from_id, end=' ')
            print('для ', end='')
            print(event.obj.to_id)
            print()


if __name__ == '__main__':
    main()
