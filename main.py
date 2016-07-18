import pygame, sys
from pygame.locals import *

# initialize pygame
pygame.init()

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# set up window
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('pyGame_challenge')

WHITE = (255, 255, 255)
player = pygame.image.load('starbox.png')
backGround = pygame.image.load('BG1.png')
xNull= 20
xCor = 20
yNull = 250
yCor = 221
direction = ''
jump = 'false'
jumpTimer = 0
fallTimer = 0
state = 'stand'
velocity_y = 0

while True:  # main game loop

    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(backGround, (0, 0))
    DISPLAYSURF.blit(player, (xCor, yCor))

    if direction == 'right' and xCor <= 250:
        xCor += 5

    if direction == 'left' and xCor >= 50:
        xCor -= 5


    if direction == 'up' and yCor >= 50:
        yCor -= 5


    if direction == 'down' and yCor <= 250:
        yCor += 5


    if jump == 'true' and jumpTimer > 0:
        yCor -= 5
        jumpTimer -= 1
        if jumpTimer <= 0:
            jump = 'false'
            fallTimer = 20

    if jump == 'false' and fallTimer > 0:
        yCor += 5
        fallTimer -= 1


    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if (event.key == K_LEFT):
                direction = 'left'
            elif (event.key == K_RIGHT):
                direction = 'right'
            elif (event.key == K_UP):
                direction = 'up'
            elif (event.key == K_DOWN):
                direction = 'down'
            elif (event.key == K_SPACE):
                jump = 'true'
                jumpTimer = 20

        elif event.type == KEYUP:
            direction = 'neutral'

    pygame.display.update()
    fpsClock.tick(FPS)
