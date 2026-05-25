import pygame
import sys
from snake import Snake
from food import Food


class Game:
    def __init__(self, width=20, height=15, cell_size=30):
        pygame.init()
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_width = width * cell_size
        self.screen_height = height * cell_size + 50  # + место для счета

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Змейка")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)

        self.snake = Snake(width // 2, height // 2)
        self.food = Food(width, height, self.snake.body)
        self.score = 0
        self.running = True
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.restart_game()
                    elif event.key == pygame.K_q:
                        self.running = False
                else:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.snake.change_direction(pygame.math.Vector2(0, -1))
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.snake.change_direction(pygame.math.Vector2(0, 1))
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.snake.change_direction(pygame.math.Vector2(-1, 0))
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.snake.change_direction(pygame.math.Vector2(1, 0))
                    elif event.key == pygame.K_q:
                        self.running = False

    def update(self):
        if not self.game_over:
            self.snake.move()

            # Проверка: съела ли змейка еду
            if self.snake.body[0] == self.food.position:
                self.snake.grow()
                self.score += 1
                self.food.respawn(self.snake.body)

            # Проверка столкновений
            if self.snake.check_collision(self.width, self.height):
                self.game_over = True

    def draw(self):
        self.screen.fill((30, 30, 30))  # темно-серый фон

        # Рисуем сетку (опционально)
        for x in range(0, self.screen_width, self.cell_size):
            pygame.draw.line(self.screen, (40, 40, 40), (x, 0), (x, self.screen_height - 50))
        for y in range(0, self.screen_height - 50, self.cell_size):
            pygame.draw.line(self.screen, (40, 40, 40), (0, y), (self.screen_width, y))

        # Рисуем змейку и еду
        self.snake.draw(self.screen, self.cell_size)
        self.food.draw(self.screen, self.cell_size)

        # Рисуем счет
        score_text = self.font.render(f"Счёт: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, self.screen_height - 40))

        if self.game_over:
            # Затемнение экрана
            overlay = pygame.Surface((self.screen_width, self.screen_height))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            # Текст Game Over
            game_over_text = self.font.render("ИГРА ОКОНЧЕНА!", True, (255, 0, 0))
            score_text = self.font.render(f"Финальный счёт: {self.score}", True, (255, 255, 255))
            restart_text = self.font.render("Нажмите R - заново или Q - выход", True, (255, 255, 255))

            self.screen.blit(game_over_text,
                             (self.screen_width // 2 - game_over_text.get_width() // 2,
                              self.screen_height // 2 - 50))
            self.screen.blit(score_text,
                             (self.screen_width // 2 - score_text.get_width() // 2,
                              self.screen_height // 2))
            self.screen.blit(restart_text,
                             (self.screen_width // 2 - restart_text.get_width() // 2,
                              self.screen_height // 2 + 50))

        pygame.display.flip()

    def restart_game(self):
        self.snake = Snake(self.width // 2, self.height // 2)
        self.food = Food(self.width, self.height, self.snake.body)
        self.score = 0
        self.game_over = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # 10 кадров в секунду (скорость игры)

        pygame.quit()
        sys.exit()