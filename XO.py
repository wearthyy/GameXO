# Крестики нолики, первый проект, 8 модуль

# Подготовка поля игры
N = '-' # Пустая клетка
X = 'x' # Крестик
O = 'o' # Нолик
game_board = [[N,N,N],
              [N,N,N],
              [N,N,N]]  # Игровая доска

# Визуализация игрового поля
def game_zone(game_board):
    game_zone = f"""
            0   1   2
    \t0 | {game_board[0][0]} | {game_board[0][1]} | {game_board[0][2]} |
    \t  -------------
    \t1 | {game_board[1][0]} | {game_board[1][1]} | {game_board[1][2]} |
    \t  -------------
    \t2 | {game_board[2][0]} | {game_board[2][1]} | {game_board[2][2]} |
    """
    return game_zone

# Изменение символов (ходы в игре)
def make_step(board, row, col, symbol):
    if board[row][col] == '-': # Проверка пуста клетка или нет
        board[row][col] = symbol # Если проверка пройдена, присваиваем символ
        return f'\nХод сделан!\n{game_zone(game_board)}\n'
    else:
        return f'\nЭта ячейка уже занята символом: {board[row][col]}\nТекущее поле выглядит так: \n{game_zone(game_board)}' # Если проверка не пройдена


# Проверка результата игры
def game_result(game_board):
    # Победа игроков
    win_x = f'\n\tПобедил игрок, играющий {X}\n\n\n'
    win_o = f'\n\tПобедил игрок, играющий {O}\n\n\n'
    its_draw = '\n\tНичья!\n\n\n'
    # Все возможные исходы
    results = [
        # проверка победы по Горизонтали
        [game_board[0][0], game_board[0][1], game_board[0][2]],
        [game_board[1][0], game_board[1][1], game_board[1][2]],
        [game_board[2][0], game_board[2][1], game_board[2][2]],
        # проверка победы по Вертикали
        [game_board[0][0], game_board[1][0], game_board[2][0]],
        [game_board[0][1], game_board[1][1], game_board[2][1]],
        [game_board[0][2], game_board[1][2], game_board[2][2]],
        # проверка победы по Диагоналям
        [game_board[0][0], game_board[1][1], game_board[2][2]],
        [game_board[0][2], game_board[1][1], game_board[2][0]],
    ]


    # Проверка условий
    for lines in results:
        if lines[0] == lines[1] == lines[2] == X:
            return win_x
        if lines[0] == lines[1] == lines[2] == O:
            return win_o

    # Проверка ничьи
    draw = True
    for row in game_board:
        for cell in row:
            if cell == N:
                draw = False
                break
    if draw:
        return its_draw

    # Игра продолжается
    return ''

while True:
    # Главное меню
    print('\n\t\tКрестики|Нолики')
    print('\tЧто бы начать игру напишите "Игра"')
    print('\tЧто бы выйти из игры напишите "Выйти"')
    game_start = input('\t\t: ').lower()
    if game_start not in ['игра', 'выйти']:
        print('\t\nПожалуйста введите корректную команду!')
        continue

    # Начало игры
    if game_start == 'игра':
        # Сброс игрового поля
        game_board = [[N, N, N],
                      [N, N, N],
                      [N, N, N]]
        while True:
            try:
                print(f'\nВведите координаты хода')
                step_row = int(input(f'Номер строки: (0-2): '))
                step_сol = int(input(f'Номер столбца: (0-2): '))
                if not (0 <= step_row <= 2) or not (0 <= step_сol <= 2):
                    print('Пожалуйста вводите верные координаты!\n')
                    continue
            except ValueError:
                print('\n\tОшибка! Введите целые числа от 0 до 2\n')
                continue
                break

            symbol = input(f'Выберите символ (O или X): ').lower()
            if symbol not in [X, O]:
                print(f'\n\tПожалуйста введите корректный символ! (X или O)\n')
                continue


            print(make_step(game_board, step_row, step_сol, symbol))

            # Проверка результата игры
            result = game_result(game_board)
            if result:
                print(result)
                break

    else:
        print('Выход из игры..')
        break
