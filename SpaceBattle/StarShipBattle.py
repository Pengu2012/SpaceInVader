import pygame
from pygame.locals import *
pygame.init()
WIDTH = 1200
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Spaceinvaders")

shipwidth = 70
shipheight = 70
border = pygame.Rect(600,0,30,600)
yellowship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("SpaceBattle/BattleShipYellow.png"),(shipwidth,shipheight)),90)
redship = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("SpaceBattle/BattleShipRed.png"),(shipwidth,shipheight)),270)
background = pygame.image.load("SpaceBattle/SpAcE.png")
yellow = pygame.Rect(20,265,shipwidth,shipheight)
red = pygame.Rect(1110,265,shipwidth,shipheight)

def draw():
    global yellow,red
    screen.blit(background,(0,0))
    screen.blit(yellowship,(yellow.x,yellow.y))
    screen.blit(redship,(red.x,red.y))

def redmovement(keypressed):
    if keypressed[pygame.K_LEFT]:
        red.x -= 1
    if keypressed[pygame.K_RIGHT]:
        red.x += 1
    if keypressed[pygame.K_UP]:
        red.y -= 1
    if keypressed[pygame.K_DOWN]:
        red.y += 1

def yellowmovement(keypressed):
    if keypressed[pygame.K_a]:
        yellow.x -= 1
    if keypressed[pygame.K_d]:
        yellow.x += 1
    if keypressed[pygame.K_w]:
        yellow.y -= 1
    if keypressed[pygame.K_s]:
        yellow.y += 1

while True:
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT: 
            exit()
    draw()
    keypressed = pygame.key.get_pressed()
    redmovement(keypressed)
    yellowmovement(keypressed)
    pygame.display.update()