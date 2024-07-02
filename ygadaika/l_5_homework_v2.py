from random import randint


def enter_range():
    a = [input('Start of range: '), input('End of range: ')]
    if 'exit' in a:
        quit()
    if a[0].isnumeric() and a[1].isnumeric() and 30 >= (int(a[1]) - int(a[0])) >= 5:
        return [int(a[0]), int(a[1])]
    else:
        print('Enter only numbers in the correct range')
        return enter_range()


def randoming_numbers(user_range_list):
    random_numbers = []
    while len(random_numbers) != 3:
        random_number = (randint(user_range_list[0], user_range_list[1]))
        if random_number in random_numbers:
            continue
        else:
            random_numbers.append(random_number)
    return random_numbers


def get_number_user(user_range):
    c = [input('First number: '), input('Second number: '), input('Third number: ')]
    user_numbers = []
    if 'exit' in c:
        quit()
    if len(c) == len(set(c)):
        for i in c:
            if i.isnumeric() and int(i) in range(user_range[0], (user_range[1] + 1)):
                user_numbers.append(int(i))
            else:
                print('Enter only numbers within the specified range!')
                return get_number_user(user_range)
    else:
        print('Your numbers are repeating')
    return user_numbers


def match_checking(numbers_random, numbers_user):
    if sorted(numbers_user) == sorted(numbers_random):
        return True
    else:
        a = 0
        for i in numbers_user:
            if i in numbers_random:
                a += 1
        print('You guessed ', a, ' numbers')


def ygadaika():
    print('Hello!\nEnter 2 numbers, the range of which must include a minimum of 5 and a maximum of 30 numbers.\n'
          'I\'ll guess 3 of them, and you guess!')
    user_range = enter_range()
    numbers_random = randoming_numbers(user_range)
    result = None
    while not result:
        result = match_checking(numbers_random, get_number_user(user_range))
    print('You Won!')


ygadaika()
