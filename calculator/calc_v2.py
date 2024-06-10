import custom_exceptions

CALCULATION_OPERATIONS = ('+', '-', '*', '/', '**')


def get_parameters():
    while True:
        num_one = input('Enter first num: ')
        if 'exit' in num_one:
            quit()
        num_two = input('Enter second num: ')
        if 'exit' in num_two:
            quit()
        operation = input('Enter operation: ')
        if 'exit' in operation:
            quit()
        try:
            float(num_one)
            float(num_two)
            if operation not in CALCULATION_OPERATIONS:
                raise custom_exceptions.UnknownOperation
            elif num_two == '0' and operation == '/':
                raise ZeroDivisionError
        except ValueError:
            print('Value entry error. Enter numbers only')
            continue
        except custom_exceptions.UnknownOperation as f:
            print(f)
            continue
        except ZeroDivisionError:
            print('You can\'t divide by zero!')
            continue
        else:
            return float(num_one), float(num_two), operation


def perform_a_mathematical_operation(parameters):
    if parameters[2] == '+':
        return parameters[0] + parameters[1]
    elif parameters[2] == '-':
        return parameters[0] - parameters[1]
    elif parameters[2] == '*':
        return parameters[0] * parameters[1]
    elif parameters[2] == '/':
        return parameters[0] / parameters[1]
    elif parameters[2] == '**':
        return parameters[0] ** parameters[1]


def app():
    print('Welcome to the Calculator.\n'
          'Available operations:\n'
          'addition "+"\n'
          'subtraction "-"\n'
          'multiplication "*"\n'
          'division "/"\n'
          'exponentiation "**"\n'
          'To exit the program, enter: "exit".')
    while True:
        print(perform_a_mathematical_operation(get_parameters()))


app()
