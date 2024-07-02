def check_users_email(user_email, users_data):
    """Принимаем введенные пользователем емеил при логининге
    проверяем правильность данных, если есть совпадение возвращаем True
    иначе False"""
    for i in users_data:
        if i.get('email') == user_email:
            return True
    return False


def check_users_password(user_email, user_password, users_data):
    """Принимаем введенные пользователем пароль при логининге
    проверяем правильность данных, если есть совпадение возвращаем True
    иначе False"""
    for i in users_data:
        if i.get('email') == user_email and i.get('password') == user_password:
            return True
    return False
