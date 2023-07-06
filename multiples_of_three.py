def multiples_of_three():
    data = [int(i) for i in input('Введите список чисел: ').split()]
    for i in data:
        if i % 3 == 0:
            print(i, end=' ')


if __name__ == '__main__':
    multiples_of_three()
