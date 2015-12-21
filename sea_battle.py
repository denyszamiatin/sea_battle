# coding=utf-8
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

def shoot_result(board, x, y):
    """
    При попадании в корабль отметить корабль как сбитый
    При промахе, отметить клетку как обстрелянную

    >>> board = [[0,0,0], [0,0,0], [0,0,0]]
    >>> add_ship(board, 1, 0)
    >>> shoot_result(board, 0, 0)
    '*'
    >>> shoot_result(board, 1, 0)
    'X'

    """
    if board[x][y] == SHIP:
        board[x][y] = SHOOT
        return board[x][y]
    else:
        board[x][y] = OVERSHOOT
        return board[x][y]


def print_board_tmp(board):
    for i in range (10):
        for j in range (10):
            print board[j][i],
        print


def check_coord_for_ship_place(board,ship_coord):
    """
    Here the board with 9 1-deck ships on diagonals with coords: a1,c3,e5,g7,i9 and a10,c8,g4,i2
    >>> board=[[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    >>> check_coord_for_ship_place(board,'a1')
    False
    >>> check_coord_for_ship_place(board,'j10')
    False
    >>> check_coord_for_ship_place(board,'a2')
    False
    >>> check_coord_for_ship_place(board,'e7')
    True
    >>> check_coord_for_ship_place(board,'e3')
    True
    >>> check_coord_for_ship_place(board,'e10')
    True
    """

    if not validate_player_coord(ship_coord):
        print 'Not valid ship coordinate...'
        exit()
    # translating to inner coordinates
    converted_coord = convert_player_to_inner_coord(ship_coord)
    x,y = converted_coord
    #print x, y

    # sub-function to check near points
    def near_points_check(near_coords):
        allow_ship_place=True
        for i in near_coords:
            #x1=i[0]; y1=i[1]
            #print x1,y1
            if board[i[0]][i[1]]== SHIP:
                allow_ship_place=False
        #print allow_ship_place
        return allow_ship_place

    if x!=0 and x!=9 and y!=0 and y!=9:
        near_coords_9=[(x,y+1),(x,y),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1),(x+1,y+1),(x+1,y),(x+1,y-1)]
        #print '9_points_for_check', near_coords_9
        print near_points_check(near_coords_9)

    elif x==0 and y!=0 and y!=9:
        near_coords_6_x0=[(x,y+1),(x,y),(x,y-1),(x+1,y+1),(x+1,y),(x+1,y-1)]
        #print 'x0_6_points_for_check', near_coords_6_x0
        print near_points_check(near_coords_6_x0)

    elif x==9 and y!=0 and y!=9:
        near_coords_6_x9=[(x,y+1),(x,y),(x,y-1),(x-1,y+1),(x-1,y),(x-1,y-1)]
        #print 'x9_6_points_for_check', near_coords_6_x9
        print near_points_check(near_coords_6_x9)

    elif y==0 and x!=0 and x!=9:
        near_coords_6_y0=[(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)]
        #print 'y0_6_points_for_check', near_coords_6_y0
        print near_points_check(near_coords_6_y0)

    elif y==9 and x!=0 and x!=9:
        near_coords_6_y9=[(x-1,y),(x,y),(x+1,y),(x-1,y-1),(x,y-1),(x+1,y-1)]
        #print 'y9_6_points_for_check', near_coords_6_y9
        print near_points_check(near_coords_6_y9)

    elif x==0 and y==0:
        near_coords_4_x0y0=[(x,y),(x+1,y),(x,y+1),(x+1,y+1)]
        #print 'x0y0_4_points_for_check', near_coords_4_x0y0
        print near_points_check(near_coords_4_x0y0)

    elif x==9 and y==0:
        near_coords_4_x9y0=[(x-1,y),(x,y),(x-1,y+1),(x,y+1)]
        #print 'x0y0_4_points_for_check', near_coords_4_x9y0
        print near_points_check(near_coords_4_x9y0)

    elif x==9 and y==9:
        near_coords_4_x9y9=[(x-1,y),(x,y),(x,y-1),(x-1,y-1)]
        #print 'x9y9_4_points_for_check', near_coords_4_x9y9
        print near_points_check(near_coords_4_x9y9)

    elif x==0 and y==9:
        near_coords_4_x0y9=[(x+1,y),(x,y),(x,y-1),(x+1,y-1)]
        #print 'x0y9_4_points_for_check', near_coords_4_x0y9
        print near_points_check(near_coords_4_x0y9)


if __name__ == '__main__':
    print "Start battle..."
    print_ship(board)
    print

    board=[[1, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print 'Here the board with 9 1-deck ships on diagonals with coords: a1,c3,e5,g7,i9 and a10,c8,g4,i2'
    print_board_tmp(board)
    print
    print 'Checking e10 coordinate:'
    check_coord_for_ship_place(board,'e10')
    print 'Checking bad e11 coordinate:'
    check_coord_for_ship_place(board,'e11')

