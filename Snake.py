
import pygame
from pygame.sprite import Sprite


class Snake(Sprite):
    def __init__(self, ai_settings, screen):
        super(Snake, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(300, 300, ai_settings.snake_width, ai_settings.snake_height)
        self.color = ai_settings.snake_color
        self.speed_factor = ai_settings.snake_speed_factor
        self.ai_settings = ai_settings
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.height_allowed = ai_settings.screen_height
        self.width_allowed = ai_settings.screen_width
        self.snk_list = []
        self.list_len = 15
        self.moving_right = False
        self.moving_left = True
        self.moving_up = False
        self.moving_down = False

    # Check snake should not go out
    def check_snake(self):
        if self.y < 0:
            self.y = self.height_allowed
        if self.y > self.height_allowed:
            self.y = 0
        if self.x < 0:
            self.x = self.width_allowed
        if self.x > self.width_allowed:
            self.x = 0

    # Move snake
    def update(self):
        self.check_snake()
        self.snk_head = []
        self.snk_head.append(self.x)
        self.snk_head.append(self.y)
        self.snk_list.append(self.snk_head)
        if len(self.snk_list) > self.list_len:
            del self.snk_list[0]
        if self.moving_right:
            self.x += self.speed_factor
            self.rect.x = self.x
        if self.moving_left:
            self.x -= self.speed_factor
            self.rect.x = self.x
        if self.moving_up:
            self.y -= self.speed_factor
            self.rect.y = self.y
        if self.moving_down:
            self.y += self.speed_factor
            self.rect.y = self.y

    # Draw snake
    def draw_snake(self, x, y):
        pygame.draw.rect(self.screen, self.color, (x, y, self.ai_settings.snake_width, self.ai_settings.snake_height))
