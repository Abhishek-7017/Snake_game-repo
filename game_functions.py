import pygame
import sys
from pygame.sprite import Group


def update_screen(ai_settings, screen, sn, fr, sb):
    screen.fill(ai_settings.bg_color)
    """if len(sn.snk_list) > sn.list_len:
        del sn.snk_list[0]"""
    for x,y in sn.snk_list:
        sn.draw_snake(x,y)
    fr.draw_fruit()
    sb.show_score()
    pygame.display.flip()


def check_event(sn):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            check_keydown_event(sn, event)


def check_keydown_event(sn, event):
    if event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_DOWN:
        sn.moving_down = True
        sn.moving_up = False
        sn.moving_right = False
        sn.moving_left = False
    elif event.key == pygame.K_UP:
        sn.moving_down = False
        sn.moving_up = True
        sn.moving_right = False
        sn.moving_left = False
    elif event.key == pygame.K_LEFT:
        sn.moving_down = False
        sn.moving_up = False
        sn.moving_right = False
        sn.moving_left = True
    elif event.key == pygame.K_RIGHT:
        sn.moving_down = False
        sn.moving_up = False
        sn.moving_right = True
        sn.moving_left = False


def update_fruit(ai_settings, sn, fr, stats, sb):
    snakes = Group()
    snakes.add(sn)
    fruits = Group()
    fruits.add(fr)
    collision = pygame.sprite.groupcollide(snakes, fruits, False, True)
    if collision:
        fr.new_fruit()
        stats.score += ai_settings.fruit_point
        sb.prep_score()
        sn.list_len += 15
        ai_settings.snake_speed_factor += 0.2
