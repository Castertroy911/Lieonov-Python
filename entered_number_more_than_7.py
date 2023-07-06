def is_number_more_7():
    entered_number = int(input(f'Пожалуйста, введите любое число: '))
    if entered_number > 7:
        print('Привет')
    else:
        print('Число меньше или равно 7')


if __name__ == '__main__':
    is_number_more_7()
