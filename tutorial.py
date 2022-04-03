import pygame
import os

WIDTH, HEIGHT = 900, 500 #Създават се променливи за ширина и височина на прозореца;
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) #Променливите се вкарват във вградената функция. Тук на тяхно място могат направо да се вкарат числени стойности, но е по-лесно с променливи, тъй като ако решим да променим нещо, трябва да променим само на едно място, не навсякъде;
#pygame.display.set.caption("First Game!")

WHITE = (255, 255, 255) #Прави се променлива, която да задава цветовете;

FPS = 60 #Задава се скорост, с която да върви играта;

#YELLOW_SPACESHIP_IMAGE = pygame.image.load(
#    os.path.join('Assets', 'spaceship_yellow.png'))
#RED_SPACESHIP_IMAGE = pygame.image.load(
#    os.path.join('Assets', 'spaceship_red.png'))


def draw_window():
    WIN.fill(WHITE) #Задава се цвета на фона да е като цвета на променливата, отново като при ред 5;
#    WIN.blit(YELLOW_SPACESHIP_IMAGE, (300, 100))
    pygame.display.update() #Ъпдейтва дисплея след всяка промяна, иначе нищо няма да се покаже;


def main():
    clock = pygame.time.Clock()
    run = True #Задаваме прозорецът да стои постоянно отворен;
    while run:
        clock.tick(FPS) #Задаваме на всички устройства играта да върви с еднаква скорост;
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False #За последните 3 реда: Прозорецът да се затваря само, ако се натисне X;

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()