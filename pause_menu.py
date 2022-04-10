import pygame, pygame_menu
from new_menu import start_the_game


def pause_menu():
    PAUSE = pygame_menu.Menu('Would you like to keep playing?', 625, 375, theme=pygame_menu.themes.THEME_DARK)
    PAUSE.add.button('Continue', start_the_game())
    PAUSE.add.button('Quit', pygame_menu.events.QUIT)
