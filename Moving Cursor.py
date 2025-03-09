import pygame

pygame.init()

screen_width = 700
screen_height = 500


screen = pygame.display.set_mode((screen_width,screen_height))

Tamil_Nadu = True


# bg_color = pygame.Color((255,243,0))
bg_color = pygame.Color((255,243,0))



while Tamil_Nadu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tamil_Nadu = False



    mouse_x, mouse_y = pygame.mouse.get_pos()

    screen.fill(bg_color)

    pygame.draw.circle(screen, "blue", (mouse_x, mouse_y), 20)

    pygame.display.flip()
