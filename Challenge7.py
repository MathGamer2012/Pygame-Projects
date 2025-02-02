import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

image = pygame.image.load("img.jpg")
x = 0
y = 0
x_vel = 1
y_vel = 1 

FPS = 1000
fpsClock = pygame.time.Clock() 

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

BLACK = [0, 0, 0]

    
font = pygame.font.Font('./text.ttf', 20)

direct = 1

quitVar = True

while quitVar == True:
    screen.fill(BLACK)
    screen.blit(image, (x, y))

    
    if direct == 1:
        x += 1

        if x >= (400-image.get_width()):
            direct = 2
    
    elif direct == 2: 
        y += 1
        x -= 1 

        if x <= (50-image.get_height()) and y >= (400-image.get_height()):
            direct = 3

    elif direct == 3:
        x += 1

        if x >= (400-image.get_width()):
            direct = 4

    elif direct == 4:
        x -= 1
        y -= 1 

        if y <= (50-image.get_height()) and x <= (50-image.get_height()):
            x = 0
            y = 0
            direct = 1 
       
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit() 
