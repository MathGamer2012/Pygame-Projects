import pygame

pygame.init()

pygame.display.set_caption("Sound Board") 

screen = pygame.display.set_mode((650,350))

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

RED = [255, 0, 0]

BLUE = [0, 0, 255]

PURPLE = [255, 0, 255] 

BLACK = [0,0,0] 

YELLOW = [255,255,0] 

ORANGE = [255,165,0] 

show = True 

font = pygame.font.Font('./text.ttf', 20)

effect = pygame.mixer.Sound("slap.mp3")
effect2 = pygame.mixer.Sound("oof.mp3")
effect3 = pygame.mixer.Sound("shot.mp3")
effect4 = pygame.mixer.Sound("bird.mp3")
effect5 = pygame.mixer.Sound("nic.mp3")
effect6 = pygame.mixer.Sound("effect6.mp3") 



myText = ""
myText2 = ""
myText3 = ""
myText4 = ""
myText5 = ""
myText6 = ""

quitVar = True

while quitVar == True:
    screen.fill(BLACK)


    if show == True:
        red_rect = pygame.draw.rect(screen, RED, (50, 50, 150, 100))
        blue_rect = pygame.draw.rect(screen, BLUE, (250, 50, 150, 100))
        green_rect = pygame.draw.rect(screen, GREEN, (450, 50, 150, 100))
        purple_rect = pygame.draw.rect(screen, PURPLE, (50, 200, 150, 100))
        orange_rect = pygame.draw.rect(screen, ORANGE, (250, 200, 150, 100))
        yellow_rect = pygame.draw.rect(screen, YELLOW, (450, 200, 150, 100))
        
        text = font.render(myText, True, BLACK)
        textRect = text.get_rect(center = (120, 100))
        screen.blit(text, textRect) 
        myText = "Slap"

        text2 = font.render(myText2, True, BLACK)
        textRect2 = text2.get_rect(center = (320, 100))
        screen.blit(text2, textRect2) 
        myText2 = "Nope"

        text3 = font.render(myText3, True, BLACK)
        textRect3 = text3.get_rect(center = (520, 100))
        screen.blit(text3, textRect3) 
        myText3 = "Gun Shot"

        text4 = font.render(myText4, True, BLACK)
        textRect4 = text4.get_rect(center = (120, 250))
        screen.blit(text4, textRect4) 
        myText4 = "Stab"

        text5 = font.render(myText5, True, BLACK)
        textRect5 = text5.get_rect(center = (320, 250))
        screen.blit(text5, textRect5) 
        myText5 = "Noice"

        text6 = font.render(myText6, True, BLACK)
        textRect6 = text6.get_rect(center = (520, 250))
        screen.blit(text6, textRect6) 
        myText6 = "Oof"
        

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if red_rect.collidepoint(position):
                effect.play()
            if blue_rect.collidepoint(position):
                effect2.play()
            if green_rect.collidepoint(position):
                effect3.play()
            if purple_rect.collidepoint(position):
                effect4.play()
            if orange_rect.collidepoint(position):
                effect5.play()
            if yellow_rect.collidepoint(position):
                effect6.play()


    pygame.display.update()

pygame.quit() 
