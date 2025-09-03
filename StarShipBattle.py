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
bulletvelocity = 7
fps = 60
velocity = 2

def draw(red,yellow,redbullet,yellowbullet):
    screen.blit(background,(0,0))
    screen.blit(yellowship,(yellow.x,yellow.y))
    screen.blit(redship,(red.x,red.y))
    for i in yellowbullet:
        pygame.draw.rect(screen,"yellow",i)
    for j in redbullet:
        pygame.draw.rect(screen,"red",j)
    pygame.display.update()

def redmovement(keypressed,red):
    if keypressed[pygame.K_LEFT]:
        red.x -= 1
    if keypressed[pygame.K_RIGHT]:
        red.x += 1
    if keypressed[pygame.K_UP]:
        red.y -= 1
    if keypressed[pygame.K_DOWN]:
        red.y += 1

def yellowmovement(keypressed,yellow):
    if keypressed[pygame.K_a]:
        yellow.x -= 1
    if keypressed[pygame.K_d]:
        yellow.x += 1
    if keypressed[pygame.K_w]:
        yellow.y -= 1
    if keypressed[pygame.K_s]:
        yellow.y += 1

def handlebullets(red,yellow,redbullet,yellowbullet):
    for i in yellowbullet:
        i.x += bulletvelocity
        if red.colliderect(i):
           print("The red ship got hit!")
           pygame.display.update()
    
    for j in redbullet:
        j.x -= bulletvelocity
        if yellow.colliderect(j):
            print("The yellow ship got hit")
            pygame.display.update()

def main():
    red = pygame.Rect(700,250,60,40)
    yellow = pygame.Rect(500,250,60,40)
    yellowbullet = []
    redbullet = []

    while True:
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT: 
                exit()
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LSHIFT:
                bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2-2,10,5)
                yellowbullet.append(bullet)
            if i.key == pygame.K_RSHIFT:
                bullet = pygame.Rect(red.x+red.width,red.y+red.height//2-2,10,5)
                redbullet.append(bullet)
        
        keypressed = pygame.key.get_pressed()
        redmovement(keypressed,red)
        yellowmovement(keypressed,yellow)
        handlebullets(red,yellow,redbullet,yellowbullet)
        draw(red,yellow,redbullet,yellowbullet)
        pygame.display.update()

main()