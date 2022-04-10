import pygame
from pause_menu import pause_menu

pygame.init()

end_game = pygame.USEREVENT + 0
pygame.time.set_timer(end_game, 1000)

while True:
    for event in pygame.event.get():
        if event.type == end_game:
            pause_menu()