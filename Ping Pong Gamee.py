import pygame
import random
pygame.init()

screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width,screen_height))

Tamil_Nadu = True
rectx,recty = 140,585

speed = 1
# bg_color = pygame.Color((255,243,0))
bg_color = pygame.Color(('black'))
clock  = pygame.time.Clock()

circx,circy = 10,10
speedx,speedy = 1,0.5

font = pygame.font.Font(None,30)

score = 0

while Tamil_Nadu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tamil_Nadu = False


    keys = pygame.key.get_pressed()
    if (keys[pygame.K_d]) and  paddle.right + 80 <= screen_width:
        rectx += speed
    if (keys[pygame.K_a]) and paddle.left >= 0:
        rectx -=speed


    circx += speedx
    circy += speedy

    if circx + 10 > screen_width or circx - 10 < 0:
        speedx = -speedx

    if circy - 10 < 0:
        speedy = -speedy

    if circy + 10 > screen_height:
        circx = random.choice([500,10])
        circy= 10


    paddle = pygame.Rect(rectx, recty, 80, 10)
    ball = pygame.Rect(circx,circy,10,10)



    if ball.colliderect(paddle):
        speedy = -speedy
        score = score+1



    screen.fill(bg_color)

    pygame.draw.rect(screen,'white',paddle)
    pygame.draw.circle(screen,'white',(circx,circy),10)


    text =  font.render(f" Score:{ score }",True,'red')
    screen.blit(text,(screen_width - 100,10))


    clock.tick(600)

    pygame.display.update()
