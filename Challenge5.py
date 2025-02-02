import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((240,180))

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

BLUE = [0, 0, 255]


font = pygame.font.Font('./text.ttf', 20)


quitVar = True

while quitVar == True:
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (120,90, 20, 40))
    pygame.draw.rect(screen, BLUE, (120,90, 20, 40), 4)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit() 
