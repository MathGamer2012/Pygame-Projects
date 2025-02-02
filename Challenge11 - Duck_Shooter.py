import pygame
import random

class Bird:
    def __init__(self):
        self.value = random.choice(["left","right"])
        self.x = ""
        self.y = "" 
        self.image = ""
        if self.value == "left":
            self.x = random.randint(50, 70)
            self.y = random.randint(100, 300)
            self.image = pygame.image.load("img-bird.png")
        else:
            self.x = random.randint(300,350)
            self.y = random.randint(100, 300)
            self.image = pygame.image.load("img-bird2.png")

    def fly(self, screen):
        if self.value == "left":
            self.y -= 1
            self.x += 1
        else:
            self.y -= 1
            self.x -= 1 
        
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        screen.blit(self.image,self.rect)
#--------------------------- end of class -----------------------------------
pygame.init()

pygame.display.set_caption("DUCK SHOOTER") 

screen = pygame.display.set_mode((400,400))

font = pygame.font.Font('./text.ttf', 20)

WHITE = [0, 0, 0]

GREEN = [0, 255, 0] 

bg = pygame.image.load("bg-bird.jpg")

FPS = 40
fpsClock = pygame.time.Clock() 

myBirds = [Bird(), Bird()]

counter = 0
timer = 0
effect = pygame.mixer.Sound("shot.mp3")
effect2 = pygame.mixer.Sound("bird.mp3") 

myText = ""
myText2 = ""
myText3 = ""
hits = 0
shots = 0
check = False


quitVar = True

while quitVar == True:
    screen.fill(WHITE)
    screen.blit(bg, (0,0))

    text3 = font.render(myText3, True, GREEN)
    textRect3 = text3.get_rect(center = (200, 30))
    screen.blit(text3, textRect3)
     

    counter += 1
    timer += 1 
    if counter == 50:
        myNewBird = Bird()
        myBirds.append(myNewBird)
        myNewBird2 = Bird()
        myBirds.append(myNewBird2)
        counter = 0

    if timer == 500:
        myText3 = "Times Up"
        myBirds.clear()
        check = True 
        
            
        
    if check == False: 
        for bird in myBirds:
            bird.fly(screen)

    text = font.render(myText, True, GREEN)
    textRect = text.get_rect(center = (100, 350))
    screen.blit(text, textRect)

    text2 = font.render(myText2, True, GREEN)
    textRect2 = text2.get_rect(center = (300, 350))
    screen.blit(text2, textRect2)

    myText = "Shots:" + str(shots) 
    myText2 = "Hits:" + str(hits) 
        
    for event in pygame.event.get():
      

        if event.type == pygame.QUIT:
            quitVar = False

        if check == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                shots += 1
                effect.play() 

                for i in range(len(myBirds)):
                    if myBirds[i].rect.collidepoint(position):
                        hits += 1
                        effect2.play() 
                        del myBirds[i]
                        break


    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit() 
