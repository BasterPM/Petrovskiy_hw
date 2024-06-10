import getters
import validators
import registration


def app():
    while True:
        users_data = getters.reading_users_data()
        user_choice = getters.get_user_response('Would you like to log in or register?\nl/r: ')
        if user_choice == 'l':
            while True:
                user_email = getters.get_user_response('Enter your email: ')
                check_email = validators.check_users_email(user_email, users_data)
                user_password = getters.get_user_response('Enter your password: ')
                check_password = validators.check_users_password(user_email, user_password, users_data)
                if check_email and check_password:
                    print('Login completed')
                    break
                else:
                    print('The email or password was entered incorrectly. '
                          'Try again or enter an \'exit\' to exit')
        elif user_choice == 'r':
            while True:
                user_email_reg = getters.get_user_response('Indicate your email: ')
                check_email = validators.check_users_email(user_email_reg, users_data)
                if not check_email:
                    user_password_new = getters.get_user_response('Create a password: ')
                    user_password_rep_new = getters.get_user_response('Repeat password: ')
                    if user_password_new == user_password_rep_new:
                        new_user = {'email': user_email_reg, 'password': user_password_new}
                        users_data.append(new_user)
                        registration.added_new_user(users_data)
                        print('Congratulations, you have successfully registered')
                        break
                else:
                    print('This email is already registered')
                    break


app()
