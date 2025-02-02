import pygame

pygame.init()

pygame.display.set_caption("Rectangle To Circle") 

screen = pygame.display.set_mode((400,400))


WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

BLACK = [0, 0, 0]

FPS = 10
fpsClock = pygame.time.Clock() 
    
font = pygame.font.Font('./text.ttf', 20)

circle = 0

quitVar = True

while quitVar == True:
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (150, 150, 150, 150), width=0, border_radius=circle)
    circle += 1

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

    fpsClock.tick(FPS)


pygame.quit() 
