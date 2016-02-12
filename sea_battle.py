# coding=utf-8
import itertools

BOARD_SIZE = 10
EMPTY_CELL = 0
SHIP = 1
SHOOT = 'X'
OVERSHOOT = '*'
X_COORD_RANGE = 'abcdefghij' # диапазон значений по x


board = [[EMPTY_CELL] * BOARD_SIZE for i in range(BOARD_SIZE)]


def add_ship(board, x, y):
    """
    Add ship to board
    >>> board = [[0,0], [0,0]]
    >>> add_ship(board, 0, 0)
    >>> board[0][0]
    1
    """
    board[x][y] = SHIP


def validate_player_coord(coord):
    """
    проверка правильности координат (формат "MK", где M - в X_COORD_RANGE,
    K - в Y_COORD_RANGE)
    >>> validate_player_coord("a1")
    True
    >>> validate_player_coord('j10')
    True
    >>> validate_player_coord('E5') # кейс с координатой с заглавной буквой
    True
    >>> validate_player_coord(True)
    False
    >>> validate_player_coord(['a', '1'])
    False
    >>> validate_player_coord('a11')
    False
    >>> validate_player_coord('z1')
    False
    >>> validate_player_coord('a')
    False
    >>> validate_player_coord('ab')
    False
    """
    try:
        letter, number = coord[0].lower(), int(coord[1:])
    except (ValueError, TypeError):
        return False
    return 'a' <= letter <= 'j' and 1 <= number <= 10


def convert_player_to_inner_coord(coord):
    """
    Функция переводит полученое значение выстрела формата "МК" в формат
    координат по оси x и y
    >>> convert_player_to_inner_coord('d5')
    (3, 4)
    >>> convert_player_to_inner_coord('e7')
    (4, 6)
    >>> convert_player_to_inner_coord('a1')
    (0, 0)
    >>> convert_player_to_inner_coord('j10')
    (9, 9)
    """
    x = X_COORD_RANGE.index(coord[0])
    y = int(coord[1:]) - 1
    return x, y


def convert_inner_to_player_coord(x, y):
    """
    Функция переводит координаты из числовых значений в формат координат игрового
    поля, для сообщения пользователю о том, куда был сделан выстрел
    >>> convert_inner_to_player_coord(3, 4)
    'd5'
    >>> convert_inner_to_player_coord(4, 6)
    'e7'
    >>> convert_inner_to_player_coord(0, 0)
    'a1'
    >>> convert_inner_to_player_coord(9, 9)
    'j10'
    >>> convert_inner_to_player_coord(*convert_player_to_inner_coord('a1'))
    'a1'
    """
    letter = X_COORD_RANGE[x]
    number = y + 1
    return letter + str(number)


def is_ship_in_cell(board, x, y):
    """
    Функция проверяет, есть ли корабль в клетке с заданными координатами
    >>> board = [[0,0,0], [0,0,0], [0,0,0]]
    >>> add_ship(board, 1, 0)
    >>> is_ship_in_cell(board, 0, 0)
    False
    >>> is_ship_in_cell(board, 1, 0)
    True
    """
    return board[x][y] == SHIP


def print_ship(board):
    """
    Функция инициирует вывод игрового поля
    """
    for row in board:
        for cell in row:
                print cell,
        print


def set_shoot_result(board, x, y):
    """
    При попадании в корабль отметить корабль как сбитый
    При промахе, отметить клетку как обстрелянную

    >>> board = [[0,0,0], [0,0,0], [0,0,0]]
    >>> add_ship(board, 1, 0)
    >>> set_shoot_result(board, 0, 0)
    >>> board[0][0]
    '*'
    >>> set_shoot_result(board, 1, 0)
    >>> board[1][0]
    'X'

    """
    board[x][y] = SHOOT if is_ship_in_cell(board, x, y) else OVERSHOOT


def check_coord_for_ship_place(board, x, y):
    """
    Here the board with 9 1-deck ships on diagonals with coords: a1,c3,e5,g7,i9 and a10,c8,g4,i2
    >>> board=[[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
               [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], \
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> check_coord_for_ship_place(board, 0, 0)
    False
    >>> check_coord_for_ship_place(board, 9, 9)
    False
    >>> check_coord_for_ship_place(board, 0, 1)
    False
    >>> check_coord_for_ship_place(board, 4, 6)
    True
    >>> check_coord_for_ship_place(board, 4, 2)
    True
    >>> check_coord_for_ship_place(board, 4, 9)
    True
    """
    near_places = tuple(itertools.product(range(-1, 2), repeat=2))

    coords_to_check = [
        (x + sx, y + sy) for sx, sy in near_places
        if 0 <= x + sx <= BOARD_SIZE - 1 and 0 <= y + sy <= BOARD_SIZE - 1
    ]

    return not any([is_ship_in_cell(board, x, y) for x, y in coords_to_check])


if __name__ == '__main__':
    print "Start battle..."
    print_ship(board)
    print

    board = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print 'Here the board with 9 1-deck ships on diagonals with coords: a1,c3,e5,g7,i9 and a10,c8,g4,i2'
    print
    print 'Checking e10 coordinate:'
    check_coord_for_ship_place(board, 4, 9)

# Git test