import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((240,180))

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]


font = pygame.font.Font('./text.ttf', 20)


quitVar = True

while quitVar == True:
    screen.fill(WHITE)
    pygame.draw.polygon(screen, GREEN, ((50,30), (90,30), (120,60), (20,60)))
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit() 
