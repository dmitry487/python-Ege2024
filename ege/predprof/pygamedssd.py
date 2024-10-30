import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Игра по химии")

# Шрифты
font = pygame.font.Font(None, 36)

# Переменные игры
player_name = ""
acids = ["Соляная", "Серная", "Уксусная"]
selected_acid = None
lives = 3
wrong_choices = []
correct_reactions = {
    "Соляная": ["Металл", "Оксид"],
    "Серная": ["Металл", "Соль"],
    "Уксусная": ["Металл", "Щелочь"]
}
current_question = None

def main_menu():
    global player_name
    while True:
        screen.fill((255, 255, 255))
        text = font.render("Введите ваше имя:", True, (0, 0, 0))
        screen.blit(text, (50, 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and player_name:
                    return
            
                # Обработка ввода имени
                if event.unicode.isprintable():
                    player_name += event.unicode
        
        # Отображение введенного имени
        name_display = font.render(player_name, True, (0, 0, 0))
        screen.blit(name_display, (50, 100))
        
        pygame.display.flip()

def choose_acid():
    global selected_acid
    while True:
        screen.fill((255, 255, 255))
        text = font.render("Выберите кислоту:", True, (0, 0, 0))
        screen.blit(text, (50, 50))

        for i, acid in enumerate(acids):
            acid_text = font.render(f"{i + 1}. {acid}", True, (0, 0, 0))
            screen.blit(acid_text, (50, 100 + i * 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_2, pygame.K_3):
                    selected_acid = acids[event.key - pygame.K_1]
                    return

        pygame.display.flip()

def ask_question():
    global current_question
    current_question = "Какое вещество реагирует с " + selected_acid + "?"
    return current_question

def game_loop():
    global lives, wrong_choices
    while lives > 0:
        screen.fill((255, 255, 255))
        question_text = font.render(ask_question(), True, (0, 0, 0))
        screen.blit(question_text, (50, 50))
        
        response_text = font.render("Введите ответ:", True, (0, 0, 0))
        screen.blit(response_text, (50, 150))

        answer_input = ""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if answer_input not in correct_reactions[selected_acid]:
                            lives -= 1
                            wrong_choices.append(answer_input)
                        break
                    
                    if event.unicode.isprintable():
                        answer_input += event.unicode
            
            # Отображение введенного ответа
            answer_display = font.render(answer_input, True, (0, 0, 0))
            screen.blit(answer_display, (50, 200))
            
            pygame.display.flip()

        if lives <= 0:
            break

def show_results():
    screen.fill((255, 255, 255))
    text = font.render("Ваши результаты:", True, (0, 0, 0))
    screen.blit(text, (50, 50))

    wrong_choices_text = font.render("Неправильные ответы: " + ", ".join(wrong_choices), True, (255, 0, 0))
    screen.blit(wrong_choices_text, (50, 100))

    pygame.display.flip()
    pygame.time.wait(5000)  # Пауза для просмотра результатов

# Основной игровой цикл
main_menu()
choose_acid()
game_loop()
show_results()

pygame.quit()
