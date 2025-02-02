import pygame
import random

pygame.init()

pygame.display.set_caption("Whack A Mole") 

screen = pygame.display.set_mode((400,400))

bg = pygame.image.load("bg.png")

bg2 = pygame.image.load("bg2.jpg") 

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

PURPLE = [128,0,128]

RED = [255,0,0]

BLUE = [0,0,255]

show = True 

font = pygame.font.Font('./text.ttf', 20)

myText = ""
myText2 = ""
myText3 = ""
myText4 = ""

image = pygame.image.load("img-mole.png")
image_x = 50
image_y = 100

FPS = 40
fpsClock = pygame.time.Clock() 
    
score = 0
counter = 0
miss = 0

effect = pygame.mixer.Sound("slap.mp3")
effect2 = pygame.mixer.Sound("oof.mp3")
effect3 = pygame.mixer.Sound("end.mp3") 


quitVar = True

while quitVar == True:
    
    if miss == 3:
        screen.blit(bg2, (0,0))
        effect3.play() 

    else: 

        screen.fill(WHITE)
        screen.blit(bg, (0,0))

        if show == True:
            rect = image.get_rect()
            rect.center = (image_x, image_y) 
            screen.blit(image, rect)

        counter += 1

        if score == 25:
            myText4 = "Medium Mode!!"
            
        if score > 25 and score < 76:
            FPS = 50
            myText4 = "" 

        if score == 75:
            myText4 = "Hard Mode!!"

        if score > 75:
            myText4 = "" 
            FPS = 60

        if score == 100:
            myText4 = "Extreme Mode!!"

        if score > 100:
            myText4 = ""
            FPS = 70 
                
        if counter == 50:
            effect2.play() 
            image_x = random.randint(100, 300) 
            image_y = random.randint(100, 300)
            miss += 1
            counter = 0

        
            
    text = font.render(myText, True, PURPLE)
    textRect = text.get_rect(center = (100, 350))
    screen.blit(text, textRect)

    text2 = font.render(myText2, True, RED)
    textRect2 = text2.get_rect(center = (300, 350))
    screen.blit(text2, textRect2)

    text3 = font.render(myText3, True, BLUE)
    textRect3 = text3.get_rect(center = (200, 30))
    screen.blit(text3, textRect3)

    text4 = font.render(myText4, True, BLUE)
    textRect4 = text4.get_rect(center = (200, 80))
    screen.blit(text4, textRect4)

    myText = "Score:" + str(score)
    myText2 = "Misses:" + str(miss)
    myText3 = "Whack A Mole"
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()

            if rect.collidepoint(position):
                score += 1
                image_x = random.randint(100, 300) 
                image_y = random.randint(100, 300)
                effect.play() 
                counter = 0

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit() 
