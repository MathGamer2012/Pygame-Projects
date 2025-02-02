import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

WHITE = [0, 0, 0]

FPS = 40
fpsClock = pygame.time.Clock() 


class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = True
        self.heightCounter = 50
        self.image = pygame.image.load("img.jpg")
        self.rect = self.image.get_rect()

    def fly(self, screen):

        if self.up == True and self.heightCounter > 0:
            self.y += 1
            self.heightCounter -= 1

        elif self.up == False and self.heightCounter > 0:
            self.y -= 1
            self.heightCounter -= 1

        elif self.up == True and self.heightCounter <= 0:
            self.up = False
            self.heightCounter = 50

        elif self.up == False and self.heightCounter <= 0:
            self.up = True 
            self.heightCounter = 50

        self.x += 1

        self.rect.center = (self.x, self.y)

        screen.blit(self.image, self.rect)

quitVar = True

myMonsters = []

while quitVar == True:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Add Monster")
            x,y = pygame.mouse.get_pos()
            myNewMonster = Monster(x,y)
            myMonsters.append(myNewMonster)

        if event.type == pygame.QUIT:
            quitVar = False

    for monStar in myMonsters:
        monStar.fly(screen)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit() 
        


            
            
        
