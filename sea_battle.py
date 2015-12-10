# coding=utf-8
BOARD_SIZE = 10
EMPTY_CELL = 0
SHIP = 1
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
    x = X_COORD_RANGE.index(coord[0])
    y = int(coord[1:]) - 1
    return x, y

def x_transform_coord(x, y):
    """
    Функция переводит координаты из числовых значений в формат координат игрового
    поля, для сообщения пользователю о том, куда был сделан выстрел
    >>> x_transform_coord(3, 4)
    ('d', 5)
    >>> x_transform_coord(4, 6)
    ('e', 7)
    >>> x_transform_coord(0, 0)
    ('a', 1)
    >>> x_transform_coord(9, 9)
    ('j', 10)
    """
    x1 = X_COORD_RANGE[x]
    y1 = y + 1
    return x1, y1





