import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

FPS = 20
fpsClock = pygame.time.Clock() 

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

RED = [255, 0, 0] 


font = pygame.font.Font('./text.ttf', 20)

green_x = 80

show = True 

quitVar = True

while quitVar == True:
    screen.fill(WHITE)

    if show == True:
        red_rect = pygame.draw.rect(screen, RED, (250, 300, 50, 50))
        green_rect = pygame.draw.rect(screen, GREEN, (green_x, 315, 20, 20))

    if green_rect.colliderect(red_rect):
        show = False

    else:
        green_x += 2
        
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()
    fpsClock.tick(FPS) 
    

pygame.quit() 
