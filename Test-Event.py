import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((240,180))

WHITE = [255, 255, 255]
GREEN = [0, 255, 0]
BLACK = [0, 0, 0] 



quitVar = True

myText = "" 

while quitVar == True:
    
    screen.fill(WHITE)
    font = pygame.font.Font('./text.ttf', 20)
    text = font.render(myText, True, GREEN)
    textRect = text.get_rect(center = (120, 90))
    screen.blit(text, textRect) 

    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: 
                myText = "Space"

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                myText = "Up"

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                myText = "Down"

            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                myText = "Left"

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                myText = "Right"


    pygame.display.update()

pygame.quit() 
