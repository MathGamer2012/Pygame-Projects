import pygame

pygame.init()

pygame.display.set_caption("Maze") 

screen = pygame.display.set_mode((400,400))

FPS = 40
fpsClock = pygame.time.Clock() 

WHITE = [255, 255, 255]

GREEN = [0, 255, 0]

RED = [255, 0, 0]

BLACK = [0, 0, 0]

CYAN = [0,255,255]

player_x = 107

player_y = 0

font = pygame.font.Font('./text.ttf', 15)

myText = ""

show = True 

quitVar = True

play = True 

while quitVar == True:
    screen.fill(BLACK)
    font = pygame.font.Font('./text.ttf', 20)
    text = font.render(myText, True, CYAN)
    textRect = text.get_rect(center = (190, 50))
    screen.blit(text, textRect) 
    
    if show == True:
        ##Setting Up the Maze Blocks 
        block = pygame.draw.polygon(screen, GREEN, ((0,0), (100,0), (100, 30), (0,30)))
        block2 = pygame.draw.polygon(screen, GREEN, ((0,30), (30, 30), (30, 400), (0,400)))
        block3 = pygame.draw.polygon(screen, GREEN, ((30,170), (110, 170), (110, 230), (70,230), (70,200), (30, 200)))
        block4 = pygame.draw.polygon(screen, GREEN, ((30,280), (110, 280), (110, 330), (30,330)))
        block5 = pygame.draw.polygon(screen, GREEN, ((30,370), (240, 370), (240, 400), (30,400)))
        block6 = pygame.draw.polygon(screen, GREEN, ((150,370), (150, 245), (180, 245), (180,370)))
        block7 = pygame.draw.polygon(screen, GREEN, ((180,330), (300, 330), (300, 300), (180,300)))
        block8 = pygame.draw.polygon(screen, GREEN, ((230,310), (230, 245), (260, 245), (260,310)))
        block9 = pygame.draw.polygon(screen, GREEN, ((285,370), (285, 400), (400, 400), (400,370)))
        block10 = pygame.draw.polygon(screen, GREEN, ((350,370), (350, 0), (400, 0), (400,370)))
        block11 = pygame.draw.polygon(screen, GREEN, ((350,0), (145, 0), (145, 30), (350,30)))
        block12 = pygame.draw.polygon(screen, GREEN, ((350,170), (150, 170), (150, 200), (350,200)))
        ##T-Like Shape (Part of the maze)
        block13 = pygame.draw.polygon(screen, GREEN, ((70,70), (300, 70), (300, 130), (70,130)))
        ##Player in the Maze
        player = pygame.draw.rect(screen, RED, (player_x, player_y, 25, 25))

    if player_y < 0:
        player_y += 10

    if player_y > 375:
        player_y -= 10
        myText = "Congrats You Finsihed the Maze!"
        play = False 



    if player.colliderect(block):
        player_x = 107
        player_y = 0

    if player.colliderect(block2):
        player_x = 107
        player_y = 0

    if player.colliderect(block3):
        player_x = 107
        player_y = 0

    if player.colliderect(block4):
        player_x = 107
        player_y = 0

    if player.colliderect(block5):
        player_x = 107
        player_y = 0

    if player.colliderect(block6):
        player_x = 107
        player_y = 0

    if player.colliderect(block7):
        player_x = 107
        player_y = 0

    if player.colliderect(block8):
        player_x = 107
        player_y = 0

    if player.colliderect(block9):
        player_x = 107
        player_y = 0

    if player.colliderect(block10):
        player_x = 107
        player_y = 0

    if player.colliderect(block11):
        player_x = 107
        player_y = 0

    if player.colliderect(block12):
        player_x = 107
        player_y = 0

    if player.colliderect(block13):
        player_x = 107
        player_y = 0
       
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            quitVar = False

        if event.type == pygame.KEYDOWN and play == True:

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                player_y -= 10 

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                player_y += 10
                
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                player_x -= 10

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                player_x += 10
                

    pygame.display.update()
    fpsClock.tick(FPS) 
    

pygame.quit() 
