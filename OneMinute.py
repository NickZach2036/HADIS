import pygame, pygame_menu, os, pymunk
from new_menu import start_the_game

def timer():
    pygame.init()
    screen = pygame.display.set_mode((1250, 750))
    font = pygame.font.Font(None, 40)
    gray = pygame.Color('gray19')
    green = pygame.Color('green')
    # The clock is used to limit the frame rate
    # and returns the time since last tick.
    clock = pygame.time.Clock()
    timer = 5  # Decrease this to count down.
    dt = 0  # Delta time (time since last tick).

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        timer -= dt
        if timer <= 0:
            MENU = pygame_menu.Menu('Would you like to keep playing?', 625, 375, theme=pygame_menu.themes.THEME_DARK)
            MENU.add.button('Continue', start_the_game())
            MENU.add.button('Quit', pygame_menu.events.EXIT)

        screen.fill(gray)
        txt = font.render(str(round(timer, 2)), True, green)
        screen.blit(txt, (1100, 70))
        pygame.display.flip()
        dt = clock.tick(30) / 1000  # / 1000 to convert to seconds.


if __name__ == '__main__':
    timer()
    pygame.quit()