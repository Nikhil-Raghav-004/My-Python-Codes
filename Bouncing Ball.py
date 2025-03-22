

import pygame

pygame.init()

screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width,screen_height))


Tamil_Nadu = True
speedX,speedy = 0.1,0.4
sx,sy = 0.6,0.5
spex,spey = 0.9,0.7


circx,circly = 500,250
circX,circlY = 500,500
Xcircl,Ycircl = 500,500
# bg_color = pygame.Color((255,243,0))
bg_color = pygame.Color(('#3B44AF'))

while Tamil_Nadu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tamil_Nadu = False
    radius = 20

    screen.fill(bg_color)

    circx += speedX
    circly += speedy

    circX += sx
    circlY += sy

    Xcircl += spex
    Ycircl += spey


    if circx + radius > screen_width or  circx - radius < 0:
        speedX = -speedX
    if circly + radius > screen_height or circly - radius < 0:
        speedy = -speedy

    if circX + radius > screen_width or  circX - radius < 0:
        sx= -sx
    if circlY + radius > screen_height or circlY - radius < 0:
        sy = -sy

    if Xcircl + radius > screen_width or Xcircl - radius < 0:
        spex = -spex
    if Ycircl + radius > screen_height or Ycircl - radius < 0:
        spey = -spey


    pygame.draw.circle(screen, 'black', (circx,circly), 20)
    pygame.draw.circle(screen, 'red', (circX,circlY), 20)
    pygame.draw.circle(screen, 'Orange', (Xcircl,Ycircl), 20)



    pygame.display.flip()
