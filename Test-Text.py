import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]


font = pygame.font.Font('./text.ttf', 20)


quitVar = True

while quitVar == True:
    screen.fill(WHITE)
    text = font.render('Hello World', True, GREEN)
    textRect = text.get_rect(center = (200, 200))
    screen.blit(text, textRect)
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit() 
