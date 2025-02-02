import pygame

pygame.init()

pygame.display.set_caption("TEST") 

screen = pygame.display.set_mode((400,400))

image = pygame.image.load("img.jpg")
image_x = 0
image_y = 0
x_vel = 1
y_vel = 1 

FPS = 90
fpsClock = pygame.time.Clock() 

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

BLACK = [0, 0, 0]

    
font = pygame.font.Font('./text.ttf', 20)

direct = 1

quitVar = True

while quitVar == True:
    screen.fill(BLACK)
    screen.blit(image, (image_x, image_y))


    if direct == 1:
        image_x += 1

        if image_x >= (400-image.get_width()):
            direct = 2
    
    elif direct == 2: 
        image_y += 1

        if image_y >= (400-image.get_height()):
            direct = 3

    elif direct == 3:
        image_x -= 1

        if image_x <= (50-image.get_width()):
            direct = 4

    elif direct ==4:
        image_y -= 1

        if image_y <= (50-image.get_height()):
            image_x = 0
            image_y = 0  

        
        
         
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

    fpsClock.tick(FPS)

pygame.quit() 
