import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

RED = [255, 0, 0]

show = True 

font = pygame.font.Font('./text.ttf', 20)

effect = pygame.mixer.Sound("test.mp3")

myText = "" 

quitVar = True

while quitVar == True:
    screen.fill(WHITE)


    if show == True:
        red_rect = pygame.draw.rect(screen, RED, (150, 150, 150, 100))
        text = font.render(myText, True, GREEN)
        textRect = text.get_rect(center = (220, 200))
        screen.blit(text, textRect) 
        myText = "Play Sound"
        
        

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if red_rect.collidepoint(position):
                effect.play() 


    pygame.display.update()

pygame.quit() 
