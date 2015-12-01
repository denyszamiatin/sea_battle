# coding=utf-8
BOARD_SIZE = 10
EMPTY_CELL = 0
SHIP = 1

board = [[EMPTY_CELL] * BOARD_SIZE for i in range(BOARD_SIZE)]

"""
Согласно википедии: "Горизонтали обычно нумеруются сверху вниз, а вертикали
помечаются буквами слева направо"
диапазон значений по х
"""
X_COORD_RANGE = 'abcdefghij'


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
    """
    try:
        letter, number = coord[0].lower(), int(coord[1:])
    except (ValueError, TypeError):
        return False
    return letter in X_COORD_RANGE and 1 <= number <= 10
