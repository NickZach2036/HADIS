import pygame
import os
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1366, 708))

def start_the_game():
    # Do the job here !
    pass

mytheme = pygame_menu.themes.THEME_DARK.copy()
BACKGROUND = pygame.image.load(os.path.join('Game pixel art', 'BIGGERSpace.png'))
myimage = pygame_menu.baseimage.BaseImage(image_path=os.path.join('Game pixel art', 'BIGGERSpace.png'))
mytheme.background_color = myimage
mytheme.title_background_color=(0, 0, 0)
menu = pygame_menu.Menu('Welcome', 400, 300, theme=mytheme)

hadislogo = pygame.image.load(os.path.join('Game pixel art', 'logo.png'))
pygame.display.set_icon(hadislogo)
pygame.display.set_caption("HADIS")

menu.add.button('Play', start_the_game)
menu.add.button('Settings')
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(surface)