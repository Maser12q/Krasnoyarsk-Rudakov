import operator
import random


def prov_otv(otv, user_otv, try_again):
    global O
    if otv == user_otv:
        O += 1
        return False, 'Вы молодцы!!!', 0
    elif try_again < 3:
        try_again += 1
        return True, 'Неверно, попробуй еще', try_again
    O -= 2
    return False, f'Неверно, вот правильный ответ: {otv}', 0


ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
ops_list = ['+', '*', '-', '/', 'urav']

try_again = 0
O = 0

print(
    '''Правила:\n4 попытки\nДля мотивации я сделаю счет, он будет идти после примеров\nВерный будет добавлять 1\nНеверный забирать 2\nОкруглять до тысячных)))''')

while True:
    # Создание примера
    sim = random.choice(ops_list)
    if sim == 'urav':

        b = random.randint(-100, 100)

        if random.randint(0, 1):
            k = round(random.random() - 0.005, 2)
        else:
            k = random.randint(-100, 100)

        true_answer = -b / k
        print('Уравнение:')
        print(f'{k}x + {b} = 0')

    else:
        a, b = random.randint(-100, 100), random.randint(-100, 100)

        # обработка если b == 0, чтобы прога не вырубалась такая штука
        try:
            true_answer = ops.get(sim)(a, b)
        except ZeroDivisionError:
            b = random.randint(-1000, -1)
        finally:
            print('Пример:')
            print(f'{a} {sim} {b} = ?')

    # ответ человека
    try:
        answer = float(input('Ответ: '))
    except ValueError:
        print('Введите цифру, вы же не хотите ломать тренажер? Пожалуйста...')
        answer = float(input('Ответ: '))

    # округление чисел float
    if type(true_answer) == float:
        true_answer = round(true_answer, 3)

    isTrue, s, try_again = prov_otv(true_answer, answer, try_again)
    print(s)

    while isTrue:
        try:
            answer = float(input('Ответ: '))
        except ValueError:
            print('Введите цифру, вы же не хотите ломать тренажер? Пожалуйста...')
            answer = float(input('Ответ: '))

        isTrue, s, try_again = prov_otv(true_answer, answer, try_again)
        print(s)
    print(f'<--- Счёт: {O} --->\n')
