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
