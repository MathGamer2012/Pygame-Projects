import pygame

pygame.init()

pygame.display.set_caption("Making Shapes") 
    
screen = pygame.display.set_mode((240,180))

WHITE = [255, 255, 255]

BLACK = [0, 0, 0]

GREEN = [0, 255, 0]


print("Select one of the options: \n 1) Circle \n 2) Triangle \n 3) Square \n 4) Pentagon \n 5) Hexagon \n 6) Octagon \n 7) Imagon(QUIT)")
print("")
choice = int(input("Your Choice: "))

if choice == 1:
    print("Circle has been drawn on the pygame screen")  
    quitVar = True

    while quitVar == True:
        screen.fill(BLACK)
        pygame.draw.circle(screen, GREEN, (120,90), 50)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()

if choice == 2:
    print("Triangle has been drawn on the pygame screen")  
    quitVar = True

    while quitVar == True:
        screen.fill(BLACK)
        pygame.draw.polygon(screen, GREEN, ((50,30), (90,30), (120,60)))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()

if choice == 3:
    print("Square has been drawn on the pygame screen")  
    quitVar = True

    while quitVar == True:
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, (120,90, 120, 90))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()

if choice == 4:
    print("Pentagon has been drawn on the pygame screen")  
    quitVar = True

    while quitVar == True:
        screen.fill(BLACK)
        pygame.draw.polygon(screen, GREEN, ((100,120), (90, 90), (120, 70), (145, 90), (130, 120)))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()

if choice == 5:
    print("Hexagon has been drawn on the pygame screen")  
    quitVar = True

    while quitVar == True:
        screen.fill(BLACK)
        pygame.draw.polygon(screen, GREEN, ((100,120), (90, 90), (120, 70), (150, 80), (160, 110), (130, 130)))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()

if choice == 6:
    print("Octogon has been drawn on the pygame screen")  
    quitVar = True

    while quitVar == True:
        screen.fill(BLACK)
        pygame.draw.polygon(screen, GREEN, ((100,120), (80, 110), (90, 90), (120, 70), (150, 80),(170, 100),(160, 110), (130, 130)))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitVar = False

        pygame.display.update()
        
pygame.quit()

if choice == 6:
    print("Bye.....Bye....")
