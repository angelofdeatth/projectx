import pygame


class Snake:
    def __init__(self, start_x, start_y):
        self.body = [(start_x, start_y)]
        self.direction = pygame.math.Vector2(1, 0)  # движение вправо
        self.grow_pending = False
        self.color = (0, 255, 0)  # зеленый цвет

    def move(self):
        head_x, head_y = self.body[0]
        new_head = (head_x + int(self.direction.x),
                    head_y + int(self.direction.y))
        self.body.insert(0, new_head)

        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False

    def change_direction(self, new_direction):
        # Запрещаем разворот на 180 градусов
        if new_direction.x * -1 != self.direction.x or new_direction.y * -1 != self.direction.y:
            self.direction = new_direction

    def grow(self):
        self.grow_pending = True

    def check_collision(self, width, height):
        head = self.body[0]
        # Столкновение со стенами
        if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height:
            return True
        # Столкновение с хвостом
        if head in self.body[1:]:
            return True
        return False

    def draw(self, screen, cell_size):
        for segment in self.body:
            x = segment[0] * cell_size
            y = segment[1] * cell_size
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, self.color, rect)
            pygame.draw.rect(screen, (0, 100, 0), rect, 2)  # обводка