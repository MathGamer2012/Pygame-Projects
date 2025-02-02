import pygame

pygame.init()

pygame.display.set_caption("Hello World") 

screen = pygame.display.set_mode((400,400))


quitVar = True

while quitVar == True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit() 
