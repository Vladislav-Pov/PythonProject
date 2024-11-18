import pygame
import math

# Константы
WIDTH, HEIGHT = 1470, 890
FPS = 300
BALL_RADIUS = 10
SPEED = 10

# Инициализация Pygame
pygame.init()

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Okay?")

# Установка иконки игры
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

# Установка времени
clock = pygame.time.Clock()

# Функция для рисования мячика
def draw_ball(pos):
    pygame.draw.circle(screen, (60, 60, 60), pos, BALL_RADIUS)

# Функция для рисования прямоугольника
def draw_rect(rect_coords):
    pygame.draw.rect(screen, (255, 255, 255), rect_coords)  # Белый цвет

# Функция для вычисления скорости мячика
def Shot(start_pos, end_pos):
    dx = 0
    dy = 0
    if start_pos and end_pos:
        # Вычисляем вектор направления
        dx = end_pos[0] - start_pos[0]
        dy = end_pos[1] - start_pos[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:           
            # Нормализуем вектор направления
            dx /= distance
            dy /= distance
    return dx * SPEED, dy * SPEED

# Проверка столкновения мяча с прямоугольником
def check_collision_with_rect(ball_pos, rect_coords):
    ball_x, ball_y = ball_pos
    rect_x, rect_y, rect_width, rect_height = rect_coords

    # Проверяем столкновение с каждой стороной прямоугольника
    if (rect_x <= ball_x <= rect_x + rect_width and 
        (rect_y - 10 <= ball_y < rect_y or rect_y + rect_height < ball_y <= rect_y + rect_height + 10)):
        return True
    if (rect_y <= ball_y <= rect_y + rect_height and 
        (rect_x - 10 <= ball_x < rect_x or rect_x + rect_width < ball_x <= rect_x + rect_width + 10)):
        return True
    return False

def check_possible_shot(mouse_pos, rect_coords, rect2_coords):
    rect_x, rect_y, rect_width, rect_height = rect_coords
    rect2_x, rect2_y, rect2_width, rect2_height = rect2_coords
    if rect_x - 10 < mouse_pos[0] < rect_x + rect_width + 10 and rect_y + rect_height + 10 > mouse_pos[1] > rect_y - 10:
        return False
    elif rect2_x - 10 < mouse_pos[0] < rect2_x + rect2_width + 10 and rect2_y + rect2_height + 10 > mouse_pos[1] > rect2_y - 10:
        return False
    else:
        return True

def main():
    start = False
    running = True
    start_pos = None
    end_pos = None
    ball_x, ball_y = 0, 0
    dx, dy = 0, 0
    mouse_pos = (0, 0)  # Инициализация mouse_pos
    
    # Определяем координаты и размеры первого прямоугольника
    rect_x = WIDTH * 3 // 8
    rect_y = HEIGHT * 5 // 16
    rect_width = WIDTH // 4
    rect_height = HEIGHT // 16
    rect_coords = (rect_x, rect_y, rect_width, rect_height)
    rect_active = True  # Переменная для отслеживания состояния первого прямоугольника

    # Определяем координаты и размеры второго прямоугольника
    rect2_x = WIDTH * 3 // 8
    rect2_y = HEIGHT * 11 // 16
    rect2_width = WIDTH // 4
    rect2_height = HEIGHT // 16
    rect2_coords = (rect2_x, rect2_y, rect2_width, rect2_height)
    rect2_active = True  # Переменная для отслеживания состояния второго прямоугольника

    # Цикл игры
    while running:
        for event in pygame.event.get():
            # Проверить закрытие окна
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Начало движения нового мячика
                mouse_pos = pygame.mouse.get_pos()
                if check_possible_shot(mouse_pos, rect_coords, rect2_coords):
                    start = True
                    start_pos = mouse_pos
                    ball_x, ball_y = start_pos
                    dx, dy = 0, 0
                    # Сбрасываем состояния обоих прямоугольников на активные
                    rect_active = True
                    rect2_active = True
            elif event.type == pygame.MOUSEBUTTONUP and start_pos:  # Проверяем наличие start_pos
                # Определение направления движения
                end_pos = pygame.mouse.get_pos()
                if end_pos != start_pos:
                    dx, dy = Shot(start_pos, end_pos)
                else:
                    start = False
                start_pos = None  # Сбрасываем start_pos

        # Обновляем позицию мячика
        ball_x += dx
        ball_y += dy

        # Проверяем, вылетел ли мячик за экран
        if ball_x < 0 or ball_x > WIDTH or ball_y < 0 or ball_y > HEIGHT:
            # Если мячик вылетел за экран, появляются обои прямоугольников
            rect_active = True
            rect2_active = True

        # Проверяем столкновение с обоими прямоугольниками, если они активны
        if rect_active and check_collision_with_rect((ball_x, ball_y), rect_coords):
            # Если мяч касается первого прямоугольника, он исчезает
            rect_active = False
            if (rect_x <= ball_x <= rect_x + rect_width and 
                (rect_y - 10 <= ball_y < rect_y or rect_y + rect_height < ball_y <= rect_y + rect_height + 10)):
                dy = -dy # Отражаем мячик от горизонтальной стороны
            if (rect_y <= ball_y <= rect_y + rect_height and 
                (rect_x - 10 <= ball_x < rect_x or rect_x + rect_width < ball_x <= rect_x + rect_width + 10)):
                dx = -dx # Отражаем мячик от вертикальной стороны
        if rect2_active and check_collision_with_rect((ball_x, ball_y), rect2_coords):
            # Если мяч касается второго прямоугольника, он исчезает
            rect2_active = False
            if (rect2_x <= ball_x <= rect2_x + rect2_width and 
                (rect2_y - 10 <= ball_y < rect2_y or rect2_y + rect2_height < ball_y <= rect2_y + rect2_height + 10)):
                dy = -dy # Отражаем мячик от горизонтальной стороны
            if (rect2_y <= ball_y <= rect2_y + rect2_height and 
                (rect2_x - 10 <= ball_x < rect2_x or rect2_x + rect2_width < ball_x <= rect2_x + rect2_width + 10)):
                dx = -dx # Отражаем мячик от вертикальной стороны

        # Очищаем экран
        screen.fill((224, 235, 235))
        
        # Рисуем прямоугольники, только если они активны
        if rect_active:
            draw_rect((rect_x, rect_y, rect_width, rect_height))
        if rect2_active:
            draw_rect((rect2_x, rect2_y, rect2_width, rect2_height))

        # Рисуем мячик
        if start:
            draw_ball([int(ball_x), int(ball_y)])

        # Обновление экрана
        pygame.display.flip()

        # Держим цикл на правильной скорости
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()