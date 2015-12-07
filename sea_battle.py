# coding=utf-8
BOARD_SIZE = 10
EMPTY_CELL = 0
SHIP = 1

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


def validate_coord(coord):
    """
    проверка правильности координат (формат "MK", где M - в X_COORD_RANGE,
    K - в Y_COORD_RANGE)
    >>> validate_coord("a1")
    True
    >>> validate_coord('j10')
    True
    >>> validate_coord('E5') # кейс с координатой с заглавной буквой
    True
    >>> validate_coord(True)
    False
    >>> validate_coord(['a', '1'])
    False
    >>> validate_coord('a11')
    False
    >>> validate_coord('z1')
    False
    >>> validate_coord('a')
    False
    >>> validate_coord('ab')
    False
    """
    try:
        letter, number = coord[0].lower(), int(coord[1:])
    except (ValueError, TypeError):
        return False
    return 'a' <= letter <= 'j' and 1 <= number <= 10

"""
Для перевода формата нам нужны выдаленые ранее константы, которые
обозначают номерацию поля
"""
X_COORD_RANGE = list('abcdefghij') # диапазон значений по x
Y_COORD_RANGE = range(1, 11) ## диапазон значений по y


def transform_coord(coord):
    """
    Функция переводит полученое значение выстрела формата "МК" в формат
    координат по оси x и y
    >>> transform_coord('d5')
    (3, 4)
    >>> transform_coord('e7')
    (4, 6)
    >>> transform_coord('a1')
    (0, 0)
    >>> transform_coord('j10')
    (9, 9)
    """
    x_coord_shoot = X_COORD_RANGE.index(coord[0]) #Перевод буквы координаты Х в индекс
    y_coord_shoot = Y_COORD_RANGE.index(int(coord[1:])) #Перевод числа координаты Y в индекс
    return x_coord_shoot, y_coord_shoot