import json


def added_new_user(update_users_data):
    """Записываем данные пользователей после регистрации"""
    with open('users_data.json', 'w') as json_file:
        json.dump(update_users_data, json_file)
