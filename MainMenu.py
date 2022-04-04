import pygame
import os
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((1366, 708))

def start_the_game():
    WIGHT, HEIGHT = 1250, 750

    pygame.init()

    screen = pygame.display.set_mode([WIGHT, HEIGHT])
    LOGO = pygame.image.load(os.path.join('Game pixel art', 'logo.png'))
    pygame.display.set_icon(LOGO)
    pygame.display.set_caption("HADIS")

    DuckX = 100
    DuckY = 100

    BACKGROUND = pygame.image.load(os.path.join('Game pixel art', 'BIGGERSpace.png'))
    IMAGE = pygame.image.load(os.path.join('Game pixel art', 'lazerPointTransparent.png'))
    DUCK = pygame.image.load(os.path.join('Game pixel art', 'yellowDuckTransparent.png'))
    BIG_DUCK = pygame.transform.scale(DUCK, (100, 100))
    WIN = pygame.display.set_mode((WIGHT, HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WIN.fill((0, 0, 0))
        WIN.blit(BACKGROUND, (0, 0))

        MX, MY = pygame.mouse.get_pos()
        WIN.blit(IMAGE, (MX - 3, MY - 3))
        pygame.mouse.set_visible(False)

        WIN.blit(BIG_DUCK, (DuckX, DuckY))
        BIG_DUCK = pygame.transform.rotate(BIG_DUCK, -1)
        # if (DuckX>WIGHT): DuckX = -100

        # DuckX = DuckX + 2
        # DuckY = DuckY

        pygame.display.flip()

    pygame.quit()
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