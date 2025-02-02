import pygame

pygame.init()

pygame.display.set_caption("Emoji") 

screen = pygame.display.set_mode((400,300))

YELLOW = [255,204,51]

WHITE = [255, 255, 255]

BLACK = [0, 0, 0] 

font = pygame.font.Font('./text.ttf', 20)

quitVar = True

while quitVar == True:
    screen.fill(WHITE)
    pygame.draw.circle(screen, YELLOW, (200,150), 140)
    pygame.draw.polygon(screen, BLACK,( (140, 110), (120, 90), (140, 70), (160, 70), (180, 90), (160, 110) ))
    pygame.draw.polygon(screen, BLACK,( (240, 110), (220, 90), (240, 70), (260, 70), (280, 90), (260, 110) ))  
    pygame.draw.polygon(screen, BLACK,( (140, 220), (120, 200), (140, 180), (260, 180), (280, 200), (260, 220) ))
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit() 
