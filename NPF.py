import pygame

pygame.init()

screen = pygame.display.set_mode([500, 500])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (170, 0, 0), (250, 250), 225)
    pygame.draw.circle(screen, (255, 255, 255), (250, 250), 175)
    pygame.draw.circle(screen, (170, 0, 0), (250, 250), 125)
    pygame.draw.circle(screen, (0, 0, 128), (250, 250), 75)

    pygame.display.flip()

pygame.quit()