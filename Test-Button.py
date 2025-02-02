import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

RED = [255, 0, 0]

show = True 

font = pygame.font.Font('./text.ttf', 20)

myText = "" 


quitVar = True

while quitVar == True:
    screen.fill(WHITE)

    text = font.render(myText, True, GREEN)
    textRect = text.get_rect(center = (120, 90))
    screen.blit(text, textRect) 



    if show == True:
        red_rect = pygame.draw.rect(screen, RED, (250, 300, 50, 50))


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if red_rect.collidepoint(position):
                myText = "Clicked"

    pygame.display.update()

pygame.quit() 
