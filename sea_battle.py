# coding=utf-8
BOARD_SIZE = 10
EMPTY_CELL = 0
SHIP = 1

board = [[EMPTY_CELL] * BOARD_SIZE for i in range(BOARD_SIZE)]

# Согласно википедии: "Горизонтали обычно нумеруются сверху вниз, а вертикали помечаются буквами слева направо"
# диапазон значений по х
X_COORD_RANGE = 'abcdefghij'
# диапазон значений по у
Y_COORD_RANGE = range(1, 11)


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
    проверка правильности координат (формат "MK", где M - в X_COORD_RANGE, K - в Y_COORD_RANGE)
    >>> coord = 'a1'
    >>> validate_coord(coord)
    True
    >>> coord = 'j10'
    >>> validate_coord(coord)
    True
    >>> coord = 'E5' # кейс с координатой с заглавной буквой
    >>> validate_coord(coord)
    True
    >>> coord =  True
    >>> validate_coord(coord)
    False
    >>> coord =  ['a', '1']
    >>> validate_coord(coord)
    False
    >>> coord =  'a11'
    >>> validate_coord(coord)
    False
    >>> coord =  'z1'
    >>> validate_coord(coord)
    False
    """
    is_valid = False
    try:
        if coord[0].lower() in X_COORD_RANGE and Y_COORD_RANGE.index(int(coord[1:])) + 1:
            is_valid = True
    finally:
        return is_valid
