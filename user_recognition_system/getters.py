import json


def get_user_response(message):
    """Функция для взаимодействия с пользователем.
    Посредством аргумента message передаем пользователю
    сообщение о том что хотем от него получить"""
    answer = input(f'{message}')
    if answer == 'exit' or answer == 'quit':
        quit()
    return answer


def reading_users_data():
    """Получаем данные пользователей"""
    with open('users_data.json', 'r') as json_file:
        users_data = json.load(json_file)
    return users_data
