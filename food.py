import random
import pygame


class Food:
    def __init__(self, width, height, snake_body=None):
        self.width = width
        self.height = height
        self.color = (255, 0, 0)  # красный цвет
        self.position = self._generate_position(snake_body)

    def _generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, self.width - 1),
                   random.randint(0, self.height - 1))
            if snake_body is None or pos not in snake_body:
                return pos

    def respawn(self, snake_body=None):
        self.position = self._generate_position(snake_body)

    def draw(self, screen, cell_size):
        x = self.position[0] * cell_size
        y = self.position[1] * cell_size
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, self.color, rect)
        pygame.draw.rect(screen, (150, 0, 0), rect, 2)  # обводка