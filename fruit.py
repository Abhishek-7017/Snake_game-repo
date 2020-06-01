
import pygame
from pygame.sprite import Sprite
import random


class Fruit(Sprite):
    def __init__(self, ai_settings, screen):
        super(Fruit, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(400, 500, ai_settings.fruit_width, ai_settings.fruit_height)
        self.color = ai_settings.fruit_color
        self.rect.x = random.randint(0, ai_settings.screen_width)
        self.rect.y = random.randint(0, ai_settings.fruit_height)
        self.sw = ai_settings.screen_width
        self.sh = ai_settings.screen_height

    def draw_fruit(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def new_fruit(self):
        self.rect.x = random.randint(1, self.sw)
        self.rect.y = random.randint(1, self.sh)
        self.draw_fruit()
