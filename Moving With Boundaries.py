

import pygame

pygame.init()

screen_width = 1000
screen_height = 1000


screen = pygame.display.set_mode((screen_width,screen_height))

Tamil_Nadu = True

rect_,rectang_ = 50,50

speed = 0.9

# bg_color = pygame.Color((255,243,0))
bg_color = pygame.Color(('#3B44AF'))

while Tamil_Nadu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tamil_Nadu = False

    keys = pygame.key.get_pressed()

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and rect_ + 20 < screen_width:
        rect_ += speed
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and rect_ - 20 > 0:
        rect_ -= speed
    if (keys[pygame.K_w] or keys[pygame.K_UP]) and rectang_ - 20 > 0:
        rectang_ -= speed
    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and rectang_ + 20 < screen_height:
        rectang_ += speed
    screen.fill(bg_color)

    pygame.draw.circle(screen, 'red', (rect_, rectang_), 20)
    # pygame.draw.rect(screen,"red",(rect_,rectang_,150,20))

    pygame.display.flip()
