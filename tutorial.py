import pygame
import os

WIDTH, HEIGHT = 1250, 750 #Създават се променливи за ширина и височина на прозореца;
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Променливите се вкарват във вградената функция. Тук на тяхно място могат направо да се вкарат числени стойности, но е по-лесно с променливи, тъй като ако решим да променим нещо, трябва да променим само на едно място, не навсякъде;
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255) #Прави се променлива, която да задава цветовете;

FPS = 60 #Задава се скорост, с която да върви играта;

YELLOW_DUCK_IMAGE = pygame.image.load(
    os.path.join('Game pixel art', 'yellowDuckTransparent.png'))
GREEN_DUCK_IMAGE = pygame.image.load(
    os.path.join('Game pixel art', 'greenDuckTransparent.png'))
BLUE_DUCK_IMAGE = pygame.image.load(
    os.path.join('Game pixel art', 'blueDuckTransparent.png'))
BIG_KAMAK_IMAGE = pygame.image.load(
    os.path.join('Game pixel art', 'bigKamakTransparent.png'))
BACKGROUND_IMAGE = pygame.image.load(
    os.path.join('Game pixel art', 'BIGGERSpace.png'))

def draw_window():
    WIN.fill(WHITE) #Задава се цвета на фона да е като цвета на променливата, отново като при ред 5;
    WIN.blit(BACKGROUND_IMAGE, (0, 0))
    WIN.blit(YELLOW_DUCK_IMAGE, (WIDTH/2, HEIGHT/2))
    #WIN.blit(GREEN_DUCK_IMAGE, (GREEN_DUCK_IMAGEInfo.x, GREEN_DUCK_IMAGEInfo.y))
    WIN.blit(BLUE_DUCK_IMAGE, (100, 200))
    WIN.blit(BIG_KAMAK_IMAGE, (WIDTH/1.5, 0))
    pygame.display.update() #Ъпдейтва дисплея след всяка промяна, иначе нищо няма да се покаже;


def main():
    clock = pygame.time.Clock()
    #GREEN_DUCK_IMAGEInfo=pygame.Rect(WIDTH/2, HEIGHT/2, WIDTH/2+20, HEIGHT/2+20,)
    run = True #Задаваме прозорецът да стои постоянно отворен;
    while run:
        clock.tick(FPS) #Задаваме на всички устройства играта да върви с еднаква скорост;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #За последните 3 реда: Прозорецът да се затваря само, ако се натисне X;
        #keys=pygame.key.get_pressed()
        #if keys[pygame.K_a]:
        #    GREEN_DUCK_IMAGEInfo.x += 1

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()