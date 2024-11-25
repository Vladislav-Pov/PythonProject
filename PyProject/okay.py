# import pygame
# import math

# # Константы
# WIDTH, HEIGHT = 1470, 890
# FPS = 300
# BALL_RADIUS = 10
# SPEED = 10

# # Инициализация Pygame
# pygame.init()

# # Создание окна
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Okay?")

# # Установка иконки игры
# icon = pygame.image.load('images/icon.png').convert_alpha()
# pygame.display.set_icon(icon)

# # Установка времени
# clock = pygame.time.Clock()

# # Функция для рисования мячика
# def draw_ball(pos):
#     pygame.draw.circle(screen, (60, 60, 60), pos, BALL_RADIUS)

# # Функция для рисования прямоугольника
# def draw_rect(rect_coords):
#     pygame.draw.rect(screen, (255, 255, 255), rect_coords)  # Белый цвет

# # Функция для вычисления скорости мячика
# def Shot(start_pos, end_pos):
#     dx = 0
#     dy = 0
#     if start_pos and end_pos:
#         # Вычисляем вектор направления
#         dx = end_pos[0] - start_pos[0]
#         dy = end_pos[1] - start_pos[1]
#         distance = math.sqrt(dx ** 2 + dy ** 2)
#         if distance > 0:           
#             # Нормализуем вектор направления
#             dx /= distance
#             dy /= distance
#     return dx * SPEED, dy * SPEED

# # Проверка столкновения мяча с прямоугольником
# def check_collision_with_rect(ball_pos, rect_coords):
#     ball_x, ball_y = ball_pos
#     rect_x, rect_y, rect_width, rect_height = rect_coords

#     # Проверяем столкновение с каждой стороной прямоугольника
#     if (rect_x <= ball_x <= rect_x + rect_width and 
#         (rect_y - 10 <= ball_y < rect_y or rect_y + rect_height < ball_y <= rect_y + rect_height + 10)):
#         return True
#     if (rect_y <= ball_y <= rect_y + rect_height and 
#         (rect_x - 10 <= ball_x < rect_x or rect_x + rect_width < ball_x <= rect_x + rect_width + 10)):
#         return True
#     return False

# def check_possible_shot(mouse_pos, rect_coords, rect2_coords):
#     rect_x, rect_y, rect_width, rect_height = rect_coords
#     rect2_x, rect2_y, rect2_width, rect2_height = rect2_coords
#     if rect_x - 10 < mouse_pos[0] < rect_x + rect_width + 10 and rect_y + rect_height + 10 > mouse_pos[1] > rect_y - 10:
#         return False
#     elif rect2_x - 10 < mouse_pos[0] < rect2_x + rect2_width + 10 and rect2_y + rect2_height + 10 > mouse_pos[1] > rect2_y - 10:
#         return False
#     else:
#         return True

# def main():
#     start = False
#     running = True
#     start_pos = None
#     end_pos = None
#     ball_x, ball_y = 0, 0
#     dx, dy = 0, 0
#     mouse_pos = (0, 0)  # Инициализация mouse_pos
    
#     # Определяем координаты и размеры первого прямоугольника
#     rect_x = WIDTH * 3 // 8
#     rect_y = HEIGHT * 5 // 16
#     rect_width = WIDTH // 4
#     rect_height = HEIGHT // 16
#     rect_coords = (rect_x, rect_y, rect_width, rect_height)
#     rect_active = True  # Переменная для отслеживания состояния первого прямоугольника

#     # Определяем координаты и размеры второго прямоугольника
#     rect2_x = WIDTH * 3 // 8
#     rect2_y = HEIGHT * 11 // 16
#     rect2_width = WIDTH // 4
#     rect2_height = HEIGHT // 16
#     rect2_coords = (rect2_x, rect2_y, rect2_width, rect2_height)
#     rect2_active = True  # Переменная для отслеживания состояния второго прямоугольника

#     # Цикл игры
#     while running:
#         for event in pygame.event.get():
#             # Проверить закрытие окна
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 # Начало движения нового мячика
#                 mouse_pos = pygame.mouse.get_pos()
#                 if check_possible_shot(mouse_pos, rect_coords, rect2_coords):
#                     start = True
#                     start_pos = mouse_pos
#                     ball_x, ball_y = start_pos
#                     dx, dy = 0, 0
#                     # Сбрасываем состояния обоих прямоугольников на активные
#                     rect_active = True
#                     rect2_active = True
#             elif event.type == pygame.MOUSEBUTTONUP and start_pos:  # Проверяем наличие start_pos
#                 # Определение направления движения
#                 end_pos = pygame.mouse.get_pos()
#                 if end_pos != start_pos:
#                     dx, dy = Shot(start_pos, end_pos)
#                 else:
#                     start = False
#                 start_pos = None  # Сбрасываем start_pos

#         # Обновляем позицию мячика
#         ball_x += dx
#         ball_y += dy

#         # Проверяем, вылетел ли мячик за экран
#         if ball_x < 0 or ball_x > WIDTH or ball_y < 0 or ball_y > HEIGHT:
#             # Если мячик вылетел за экран, появляются обои прямоугольников
#             rect_active = True
#             rect2_active = True

#         # Проверяем столкновение с обоими прямоугольниками, если они активны
#         if rect_active and check_collision_with_rect((ball_x, ball_y), rect_coords):
#             # Если мяч касается первого прямоугольника, он исчезает
#             rect_active = False
#             if (rect_x <= ball_x <= rect_x + rect_width and 
#                 (rect_y - 10 <= ball_y < rect_y or rect_y + rect_height < ball_y <= rect_y + rect_height + 10)):
#                 dy = -dy # Отражаем мячик от горизонтальной стороны
#             if (rect_y <= ball_y <= rect_y + rect_height and 
#                 (rect_x - 10 <= ball_x < rect_x or rect_x + rect_width < ball_x <= rect_x + rect_width + 10)):
#                 dx = -dx # Отражаем мячик от вертикальной стороны
#         if rect2_active and check_collision_with_rect((ball_x, ball_y), rect2_coords):
#             # Если мяч касается второго прямоугольника, он исчезает
#             rect2_active = False
#             if (rect2_x <= ball_x <= rect2_x + rect2_width and 
#                 (rect2_y - 10 <= ball_y < rect2_y or rect2_y + rect2_height < ball_y <= rect2_y + rect2_height + 10)):
#                 dy = -dy # Отражаем мячик от горизонтальной стороны
#             if (rect2_y <= ball_y <= rect2_y + rect2_height and 
#                 (rect2_x - 10 <= ball_x < rect2_x or rect2_x + rect2_width < ball_x <= rect2_x + rect2_width + 10)):
#                 dx = -dx # Отражаем мячик от вертикальной стороны

#         # Очищаем экран
#         screen.fill((224, 235, 235))
        
#         # Рисуем прямоугольники, только если они активны
#         if rect_active:
#             draw_rect((rect_x, rect_y, rect_width, rect_height))
#         if rect2_active:
#             draw_rect((rect2_x, rect2_y, rect2_width, rect2_height))

#         # Рисуем мячик
#         if start:
#             draw_ball([int(ball_x), int(ball_y)])

#         # Обновление экрана
#         pygame.display.flip()

#         # Держим цикл на правильной скорости
#         clock.tick(FPS)

# if __name__ == "__main__":
#     main()
#     pygame.quit()

import pygame
import math
from constants import *

# Класс Ball управляет поведением мяча в игре
class Ball:
    def __init__(self, radius: int, speed: int):
        """
        Инициализация мяча.
        Атрибуты:
            radius: Радиус мяча.
            speed: Скорость мяча.
        """
        self.radius = radius  # Радиус мяча
        self.speed = speed  # Скорость мяча
        self.x = 0  # Координата X мяча
        self.y = 0  # Координата Y мяча
        self.dx = 0  # Скорость мяча по оси X
        self.dy = 0  # Скорость мяча по оси Y
        self.active = False  # Флаг, указывающий, находится ли мяч в движении

    def set_position(self, position: tuple[int, int]):
        """
        Устанавливает начальную позицию мяча.
        Атрибуты:
            position: Координаты начальной позиции мяча.
        """
        self.x, self.y = position
        self.dx, self.dy = 0, 0
        self.active = True

    def calculate_speed(self, start_position: tuple[int, int], end_position: tuple[int, int]):
        """
        Рассчитывает скорость движения мяча.
        Атрибуты:
            start_position: Координаты начальной точки.
            end_position: Координаты конечной точки.
        """
        dx = end_position[0] - start_position[0]
        dy = end_position[1] - start_position[1]
        distance = math.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:
            self.dx = (dx / distance) * self.speed
            self.dy = (dy / distance) * self.speed

    def move(self):
        """
        Обновляет координаты мяча в соответствии с текущей скоростью.
        """
        self.x += self.dx
        self.y += self.dy

    def check_collision(self, rectangle: tuple[int, int, int, int]) -> bool:
        """
        Проверяет столкновение мяча с прямоугольником.
        Атрибуты:
            rectangle: Координаты и размеры прямоугольника (x, y, ширина, высота).
        Возвращает: True, если произошло столкновение, иначе False.
        """
        rect_x, rect_y, rect_width, rect_height = rectangle
        if (rect_x <= self.x <= rect_x + rect_width and
            (rect_y - COLLISION_OFFSET <= self.y < rect_y or
             rect_y + rect_height < self.y <= rect_y + rect_height + COLLISION_OFFSET)):
            self.dy = -self.dy
            return True
        if (rect_y <= self.y <= rect_y + rect_height and
            (rect_x - COLLISION_OFFSET <= self.x < rect_x or
             rect_x + rect_width < self.x <= rect_x + rect_width + COLLISION_OFFSET)):
            self.dx = -self.dx
            return True
        return False

    def is_out_of_bounds(self, screen_width: int, screen_height: int) -> bool:
        """
        Проверяет, вышел ли мяч за границы игрового экрана.
        Атрибуты:
            screen_width: Ширина экрана.
            screen_height: Высота экрана.
        Возвращает: True, если мяч за границами, иначе False.
        """
        return self.x < 0 or self.x > screen_width or self.y < 0 or self.y > screen_height


# Класс Game управляет основной логикой игры
class Game:
    def __init__(self):
        """
        Инициализирует игру: настройки экрана, загрузка ресурсов, создание объектов.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание игрового экрана
        pygame.display.set_caption("Okay?")  # Установка заголовка окна
        icon = pygame.image.load('images/icon.png').convert_alpha()  # Загрузка иконки
        pygame.display.set_icon(icon)  # Установка иконки
        self.clock = pygame.time.Clock()  # Объект для управления частотой кадров
        self.ball = Ball(BALL_RADIUS, SPEED)  # Экземпляр класса Ball
        self.rect1 = self.init_rectangle(WIDTH * 3 // 8, HEIGHT * 5 // 16, WIDTH // 4, HEIGHT // 16)
        self.rect2 = self.init_rectangle(WIDTH * 3 // 8, HEIGHT * 11 // 16, WIDTH // 4, HEIGHT // 16)
        self.rect1_active = True  # Флаг активности первого прямоугольника
        self.rect2_active = True  # Флаг активности второго прямоугольника

    @staticmethod
    def init_rectangle(x: int, y: int, width: int, height: int) -> tuple[int, int, int, int]:
        """
        Создаёт прямоугольник.
        Атрибуты:
            x: Координата X прямоугольника.
            y: Координата Y прямоугольника.
            width: Ширина прямоугольника.
            height: Высота прямоугольника.
        Возвращает: Кортеж с параметрами прямоугольника.
        """
        return x, y, width, height

    def draw_ball(self):
        """
        Отрисовывает мяч на экране.
        """
        pygame.draw.circle(self.screen, BALL_COLOR, (int(self.ball.x), int(self.ball.y)), self.ball.radius)

    def draw_rectangle(self, rectangle: tuple[int, int, int, int]):
        """
        Отрисовывает прямоугольник на экране.
        Атрибуты:
            rectangle: Координаты и размеры прямоугольника.
        """
        pygame.draw.rect(self.screen, RECT_COLOR, rectangle)

    def reset_game_objects(self):
        """
        Сбрасывает состояние игровых объектов.
        """
        self.rect1_active = True
        self.rect2_active = True

    def handle_collision(self):
        """
        Проверяет и обрабатывает столкновения мяча с прямоугольниками.
        """
        if self.rect1_active and self.ball.check_collision(self.rect1):
            self.rect1_active = False
        if self.rect2_active and self.ball.check_collision(self.rect2):
            self.rect2_active = False

    def main_loop(self):
        """
        Основной игровой цикл.
        """
        running = True
        start_position = None

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Обработка выхода
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:  # Начало движения мяча
                    mouse_position = pygame.mouse.get_pos()
                    if self.can_shoot(mouse_position):
                        self.ball.set_position(mouse_position)
                        start_position = mouse_position
                elif event.type == pygame.MOUSEBUTTONUP and start_position:  # Конец движения
                    end_position = pygame.mouse.get_pos()
                    self.ball.calculate_speed(start_position, end_position)
                    start_position = None

            # Обновление состояния мяча
            if self.ball.active:
                self.ball.move()
                self.handle_collision()

            # Проверка выхода за границы
            if self.ball.is_out_of_bounds(WIDTH, HEIGHT):
                self.reset_game_objects()
                self.ball.active = False

            # Отрисовка
            self.screen.fill(BACKGROUND_COLOR)
            if self.rect1_active:
                self.draw_rectangle(self.rect1)
            if self.rect2_active:
                self.draw_rectangle(self.rect2)
            if self.ball.active:
                self.draw_ball()
            pygame.display.flip()

            self.clock.tick(FPS)  # Ограничение FPS

        pygame.quit()

    def can_shoot(self, mouse_position: tuple[int, int]) -> bool:
        """
        Проверяет, можно ли выпустить мяч из текущей позиции.
        Атрибуты:
            mouse_position: Текущая позиция мыши.
        Возвращает: True, если можно, иначе False.
        """
        return all(not self.is_inside_rectangle(mouse_position, rectangle) for rectangle in [self.rect1, self.rect2])
    
    @staticmethod
    def is_inside_rectangle(position: tuple[int, int], rectangle: tuple[int, int, int, int]) -> bool:
        """
        Проверяет, находится ли точка внутри прямоугольника.
        Атрибуты:
            position: Координаты точки.
            rectangle: Параметры прямоугольника.
        Возвращает: True, если точка внутри, иначе False.
        """
        x, y = position
        rect_x, rect_y, rect_width, rect_height = rectangle
        return rect_x - COLLISION_OFFSET <= x <= rect_x + rect_width + COLLISION_OFFSET and \
               rect_y - COLLISION_OFFSET <= y <= rect_y + rect_height + COLLISION_OFFSET


if __name__ == "__main__":
    game = Game()
    game.main_loop()