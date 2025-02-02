import pygame
import random 

class Cactus:
    def __init__(self):
        self.x = 900
        self.y = 490
        self.image = pygame.image.load("cactus.png")
        self.rect = self.image.get_rect()


    def move(self, screen):
        self.x -= 4

    def draw(self, screen):
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)        


class Cactus2:
    def __init__(self):
        self.x = 900
        self.y = 490
        self.image = pygame.image.load("cactus2.png")
        self.rect = self.image.get_rect()

    def move(self, screen):
        self.x -= 4

    def draw(self, screen):
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)


class Dino:
    def __init__(self):
        self.x = 40
        self.y = 495
        self.vel_y = 0
        self.image = pygame.image.load("dino.png")


    def draw(self, screen):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)

    def jump(self):
        self.y += self.vel_y

    
pygame.init()

pygame.display.set_caption("Dinosaur Game") 

screen = pygame.display.set_mode((900,600))

FPS = 120
fpsClock = pygame.time.Clock() 

BLUE = [135,206,235]

GREEN = [0, 255, 0]

myCacti = []
myCacti2 = []

myDino = Dino()

myText = ""
myText2 = ""
myText3 = ""
font = pygame.font.Font('./text.ttf', 40)
font2 = pygame.font.Font('./text.ttf', 20)


effect = pygame.mixer.Sound("jump.mp3")
effect2 = pygame.mixer.Sound("over.mp3")

counter = 90
score = 0 
check = False 

quitVar = True


while quitVar == True:
    screen.fill(BLUE)
    pygame.draw.rect(screen, GREEN, (0, 530, 900, 70))

    text = font.render(myText, True, GREEN)
    textRect = text.get_rect(center = (450, 300))
    screen.blit(text, textRect)

    text2 = font2.render(myText2, True, GREEN)
    textRect2 = text2.get_rect(center = (830, 20))
    screen.blit(text2, textRect2)


    if check == False:
        myDino.draw(screen)

    counter += 1

    if check == False:
        score += 1

    myText2 = "Score: " + str(score)

    if counter == 100:
        myNewCacti = Cactus()
        myCacti.append(myNewCacti)

    if counter == 250:
        myNewCacti2 = Cactus2()
        myCacti2.append(myNewCacti2)
        counter = 0

    if check == False:
        for cactus in myCacti:
            cactus.draw(screen)
            cactus.move(screen)

    if check == False:
        for cactus2 in myCacti2:
            cactus2.draw(screen)
            cactus2.move(screen)

    if myDino.y == 240:
        myDino.vel_y = 5

    if myDino.y == 495:
        myDino.vel_y = 0 

    if check == False:  
        for i in range(len(myCacti)):
            if myCacti[i].rect.colliderect(myDino.rect):
                effect2.play()
                myText = "Game Over"
                myCacti.clear()
                check = True
                
                

        for i in range(len(myCacti2)):
            if myCacti2[i].rect.colliderect(myDino.rect):
                effect2.play()
                myText = "Game Over"
                myCacti.clear()
                check = True


        
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.KEYDOWN and myDino.y == 495:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                myDino.vel_y = -5

            if check == False:
                effect.play()

                
    myDino.jump()
    

    pygame.display.update()
    fpsClock.tick(FPS)


pygame.quit() 
