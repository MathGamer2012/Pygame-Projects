import pygame

pygame.init()
pygame.display.set_caption("ADJUSTING THE SHAPES")
screen = pygame.display.set_mode((400,300))

WHITE = [255, 255, 255] 
BLACK = [0, 0,  0] 
RED = [255, 0, 0]
GREEN = [0,255,0] 
BLUE = [0,0,255] 

quitVar = True 


while quitVar == True:

    screen.fill(BLACK)
    pygame.draw.polygon(screen, BLUE, ((180,160), (170, 130), (200, 110), (225, 130), (210, 160)))
    pygame.draw.line(screen, RED, (0,10), (60,10),4)
    pygame.draw.line(screen, RED, (60,10), (0,60),4)
    pygame.draw.line(screen, RED, (0,60), (60,60),4)
    pygame.draw.circle(screen, RED, (380,20), 20, 0)
    pygame.draw.ellipse(screen,GREEN, (355, 280, 40, 8), 1)
    pygame.draw.rect(screen, GREEN, (10, 240, 100, 50))

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit() 
    


    

