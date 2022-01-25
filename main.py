board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9
         ]

# Перечень выигрышных комбинаций
winning_coords = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                 (1, 4, 7), (2, 5, 8), (3, 6, 9),
                 (1, 5, 9), (3, 5, 7)
                 ]

blue = "\033[34m"  # Цвет крестиков
red = "\033[31m"  # Цвет ноликов
black = "\033[30m"  # Цвет доски


# Рисуем доску
def draw_board():
    print(black)
    print("-" * 13)
    for i in range(3):
        # Просто немного украшательств
        first_line = str(board[i * 3])
        second_line = str(board[i * 3 + 1])
        third_line = str(board[i * 3 + 2])
        first_line = first_line.replace('X', blue+'X')
        first_line = first_line.replace('O', red + 'O')
        second_line = second_line.replace('X', blue + 'X')
        second_line = second_line.replace('O', red + 'O')
        third_line = third_line.replace('X', blue + 'X')
        third_line = third_line.replace('O', red + 'O')

        # Выводим красивую доску в консоль
        print(f"{black}| {first_line} {black}| {second_line} {black}| {third_line} {black}|")
        print("-" * 13)


def get_move(token):
    # Бесконечный цикл, прерываем на победе или ничьей
    while True:
        value_ = input(f'Ход {token}. Куда сходим? ')  # Получаем № ячейки для проставки Х или О
        if value_ not in '123456789':  # Проверяем, что ввели цифры, а не какую-то хрень
            print('Надо указать номер свободной ячейки.')
            continue
        value_ = int(value_)  # Преобразуем число в тип int
        # Проверяем, что ячейка свободна
        if str(board[value_ - 1]) in 'XO':
            print('Клетка занята, укажите номер свободной ячейки.')
            continue
        board[value_ - 1] = token  # Присваиваем ячейке крестик или нолик
        break  # Ход сделан - можно выходить из функции


def someone_won():
    for each in winning_coords:  # Проходимся по выигрышным координатам и проверяем, не совпало ли что-то
        if board[each[0] - 1] == board[each[1] - 1] == board[each[2] - 1]:
            return board[each[1] - 1]  # Если совпало, возвр. содержимое совпавшей ячейки, т.е. истину
    else:  # Если прошлись, но выигрышная позиция так и не нашлась,
        return False  # возвращаем ложь


def main():
    move_count = 0  # Просто счётчик
    while True:
        draw_board()
        if move_count % 2 == 0:  # Если счётчик чётный, значит ход крестиков
            get_move('X')
        else:  # Иначе ход ноликов
            get_move('O')

        if move_count > 3:  # Спустя три хода имеет смысл начать проверять, не выиграл ли кто-то
            winner = someone_won()
            if winner:
                draw_board()
                print(f'{winner} выиграл!')
                break
        move_count += 1
        if move_count > 8:  # Спустя восемь ходов имеет смысл начать проверять, нет ли ничьей
            draw_board()
            print('Ничья!')
            break


main()
