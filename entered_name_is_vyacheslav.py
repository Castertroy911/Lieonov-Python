def is_entered_name_vyacheslav():
    target_name = 'Вячеслав'
    entered_name = str(input(f'Пожалуйста, введите имя: '))
    if entered_name == target_name:
        print('Привет, Вячеслав')
    else:
        print('Нет такого имени')


if __name__ == '__main__':
    is_entered_name_vyacheslav()