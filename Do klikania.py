import pygame
import sys

def draw_board(board):
    myFont = pygame.font.SysFont('Calibri', screenSize // 5)
    for y in range(5):
        for x in range(5):
            if board[y][x] == xMark:
                color = xColor
            else:
                color = oColor
            text_surface = myFont.render(board[y][x], False, color)
            screen.blit(text_surface, (y * 110, x * 105 ))
    draw_lines()
def is_full(board):
    return not any(None in sublist for sublist in board)
def get_winner(board):
    if ((board[1][1] == board[2][2] and board[2][2] == board[3][3]) \
            or (board[1][3] == board[2][2] and board[2][2] == board[3][1])) and board[2][2] is not None:
        return board[2][2]
    for i in range(1,4):
        if board[i][1] == board[i][2] and board[i][2] == board[i][3] and board[i][1] is not None:
            return board[i][1]
        if board[1][i] == board[2][i] and board[2][i] == board[3][i] and board[1][i] is not None:
            return board[1][i]
    return None
def draw_lines():
    pygame.draw.line(screen, lineColor, (200,100),(200, 400), lineSize)
    pygame.draw.line(screen, lineColor, (300, 100),(300, 400), lineSize)
    pygame.draw.line(screen, lineColor, (100,200), (400,200),lineSize)
    pygame.draw.line(screen, lineColor, (100,300),(400,300), lineSize)
def draw_col_indicators(board,column):
    if column==1:
        board[1][0] = " I"
        board[1][4] = " I"
    elif column==2:
        board[2][0] = " I"
        board[2][4] = " I"
    elif column==3:
        board[3][0] = " I"
        board[3][4] = " I"
    return board
def draw_row_indicators(board,row):
    if row==1:
        board[0][1] = "-"
        board[4][1] = "-"
    elif row==2:
        board[0][2] = "-"
        board[4][2] = "-"
    elif row==3:
        board[0][3] = "-"
        board[4][3] = "-"
    return board
def cleanrows(board):
    for i in range(0,5):
        board[0][i]=None
        board[4][i]=None
    return board
def cleancolumns(board):
    for i in range(0,5):
        board[i][0] = None
        board[i][4] = None
    return board
screenSize = 500
margin = 100
lineSize = 10
column=0
row=0
backgroundColor = (0, 0, 0)
lineColor = (255, 255, 255)
xColor = (200, 0, 0)
oColor = (0, 0, 200)
xMark = 'X'
oMark = 'O'
board = [[None,None,None, None, None],
         [None,None,None, None, None],
         [None,None,None, None, None],
         [None,None,None, None, None],
         [None,None,None, None, None]]
currentMove = 'X'
pygame.init()
screen = pygame.display.set_mode((screenSize, screenSize))
pygame.display.set_caption("Tic Tac Toe")
pygame.font.init()
myFont = pygame.font.SysFont('Calibri', screenSize // 3)
screen.fill(backgroundColor)
canPlay = True
draw_lines()
WAIT = pygame.USEREVENT + 1
ti=False
ti2=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and ti==False:
            while ti2==False:
                pygame.time.set_timer(WAIT, 2000)
                ti2=True
            column=column+1
            if column>3:column=1
            screen.fill(backgroundColor)
            board=cleancolumns(board)
            board = draw_col_indicators(board,column)
            draw_board(board)
            board=cleancolumns(board)
        if event.type==WAIT and column>0:
            ti=True
            screen.fill(backgroundColor)
            board = draw_col_indicators(board,column)
            board = draw_row_indicators(board,row=1)
            draw_board(board)
        if event.type == pygame.MOUSEBUTTONDOWN and ti==True:
            row=row+1
            if row>3:row=1
            screen.fill(backgroundColor)
            board=cleanrows(board)
            board = draw_col_indicators(board,column)
            board = draw_row_indicators(board,row)
            draw_board(board)
            board=cleanrows(board)
            board=cleanrows(board)
        if event.type==WAIT and row>0:
            ti=False
            board=cleanrows(board)
            board=cleancolumns(board)
            screen.fill(backgroundColor)
            draw_board(board)
            if board[column][row] is None:
                board[column][row] = currentMove
                column=0
                row=0
                if currentMove == xMark:
                    currentMove = oMark
                else:
                    currentMove = xMark
                draw_board(board)
                winner = get_winner(board)
                if winner is not None:
                    myFont = pygame.font.SysFont('Calibri', screenSize // 5)
                    text_surface = myFont.render(str(winner) + " has won!", False, lineColor)
                    screen.blit(text_surface, (50,screenSize // 2 - screenSize // 10))
                    canPlay = False
                    pygame.time.set_timer(WAIT, 0)
                else:
                    if is_full(board):
                        myFont = pygame.font.SysFont('Calibri', screenSize // 5)
                        text_surface = myFont.render("Draw!", False, lineColor)
                        screen.blit(text_surface, (5,screenSize // 10, screenSize // 2 - screenSize // 10))

    if canPlay==False:
        board = [[None,None,None, None, None], [None,None,None, None, None], [None,None,None, None, None],[None,None,None, None, None],[None,None,None, None, None]]
        screen.fill(backgroundColor)
        draw_lines()
        ti2=False
        currentMove = 'X'
        canPlay = True
    pygame.display.update()
