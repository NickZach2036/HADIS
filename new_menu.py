import pygame
import pygame_menu
import os

pygame.init()

WIDTH = 1366
HEIGHT = 708
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

LOGO = pygame.image.load(os.path.join('Game pixel art', 'logo.png'))
pygame.display.set_icon(LOGO)
pygame.display.set_caption("HADIS")

#BACKGROUND = pygame.image.load()
#SCREEN.blit(BACKGROUND, (0, 0))

HADIStheme = pygame_menu.themes.THEME_DARK.copy()
BACKGROUND = pygame_menu.baseimage.BaseImage(image_path=os.path.join('Game pixel art', 'BIGGERSpace.png'), drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)
HADIStheme.background_color = BACKGROUND



def music(VALUE, MUSIC):
    MUSIC = True
    pass

def start_the_game():
    # Do the job here !
    pass

def about_page():
    # Do the job here !
    pass

MENU = pygame_menu.Menu('HADIS', WIDTH/2, HEIGHT/2, theme=pygame_menu.themes.THEME_DARK)
MENU.add.button('Play', start_the_game)
MENU.add.selector('Music: ', [('On', True), ('Off', False)], onchange=music)
MENU.add.button('About the game', about_page)
MENU.add.button('Quit', pygame_menu.events.EXIT)

MENU.mainloop(SCREEN)