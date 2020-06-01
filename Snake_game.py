import pygame
import game_functions as gf
from Settings import Settings
from Snake import Snake
from fruit import Fruit
from scoreboard import Score
from game_stats import GameStats


def run_game():
    # Initialize the game configuration
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Snake_game")
    sn = Snake(ai_settings, screen)
    fr = Fruit(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Score(ai_settings, screen, stats)

    while True:
        gf.check_event(sn)
        sn.update()
        gf.update_fruit(ai_settings, sn, fr, stats, sb)
        gf.update_screen(ai_settings, screen, sn, fr, sb)


if __name__ == "__main__":
    run_game()
