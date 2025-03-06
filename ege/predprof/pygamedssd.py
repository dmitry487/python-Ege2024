import pygame
import sys


WIDTH, HEIGHT = 300, 300
LINE_COLOR = (23, 145, 135)
BG_COLOR = (28, 170, 156)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
LINE_WIDTH = 15
SPACE = WIDTH // 3


pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Крестики-нолики')


board = [["" for _ in range(3)] for _ in range(3)]
player = "X"
game_over = False

def draw_board():
    screen.fill(BG_COLOR)

    pygame.draw.line(screen, LINE_COLOR, (SPACE, 0), (SPACE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (SPACE * 2, 0), (SPACE * 2, HEIGHT), LINE_WIDTH)

    pygame.draw.line(screen, LINE_COLOR, (0, SPACE), (WIDTH, SPACE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, SPACE * 2), (WIDTH, SPACE * 2), LINE_WIDTH)

def draw_figures():
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, CROSS_COLOR, (col * SPACE + SPACE // 4, row * SPACE + SPACE // 4),
                                 (col * SPACE + SPACE - SPACE // 4, row * SPACE + SPACE - SPACE // 4), LINE_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SPACE + SPACE - SPACE // 4, row * SPACE + SPACE // 4),
                                 (col * SPACE + SPACE // 4, row * SPACE + SPACE - SPACE // 4), LINE_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR,
                                   (col * SPACE + SPACE // 2, row * SPACE + SPACE // 2), SPACE // 3, LINE_WIDTH)

def check_winner():
    global game_over

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            game_over = True
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            game_over = True
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != "":
        game_over = True
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        game_over = True
        return board[0][2]


    if all(cell != "" for row in board for cell in row):
        game_over = True

    return None

def reset_game():
    global board, player, game_over
    board = [["" for _ in range(3)] for _ in range(3)]
    player = "X"
    game_over = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = mouseY // SPACE
            clicked_col = mouseX // SPACE

            if board[clicked_row][clicked_col] == "":
                board[clicked_row][clicked_col] = player
                player = "O" if player == "X" else "X"
                winner = check_winner()
                if winner:
                    print(f"Победитель: {winner}")
                elif game_over:
                    print("Ничья!")

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            reset_game()

    draw_board()
    draw_figures()

    if game_over:
        font = pygame.font.Font(None, 36)
        text = font.render("Нажмите R для перезапуска", True, (255, 255, 255))
        screen.blit(text, (WIDTH // 6, HEIGHT // 2))

    pygame.display.update()
