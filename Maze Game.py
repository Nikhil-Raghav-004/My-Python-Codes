import pygame

pygame.init()

screen_width = 800
screen_height = 601


screen = pygame.display.set_mode((screen_width,screen_height))

Tamil_Nadu = True


tile_siZe = 40
red = pygame.Color('red')
black = pygame.Color('black')
# bg_color = pygame.Color((255,243,0))
bg_color = pygame.Color((0 , 128, 250))

maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,20,0,0,0,0,0,0,0,1,0,0,0,50,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1],
    [1,1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,1],
    [1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,50,1,0,0,0,0,1,0,0,0,1,0,1],
    [1,0,1,0,1,1,1,0,1,1,1,1,0,1,1,1,1,1,0,1],
    [1,0,1,50,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,50,0,0,1],
    [1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,10,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],

]
player_row,player_coloumn = 1,1 # players Starting position
wall = pygame.image.load("Python Wall textrue.jpg")
wall = pygame.transform.scale(wall,(tile_siZe,tile_siZe))

path = pygame.image.load("Python Grass.png")
path = pygame.transform.scale(path,(tile_siZe,tile_siZe))

coins = pygame.image.load("Coins.png")
coins = pygame.transform.scale(coins,(50,50))

start = pygame.image.load("flag_bg2.png")
start = pygame.transform.scale(start,(tile_siZe+10,tile_siZe+10))

ending = pygame.image.load("Ending for Maze.png")
ending = pygame.transform.scale(ending,(tile_siZe,tile_siZe))

player = pygame.image.load("image-removebg-preview.png")
player = pygame.transform.scale(player,(50,40))



for i in range(len(maze)):
    for j in range(len(maze[0])):
        print(maze[i][j],end = "   ")
    print("\n")



score = 0


while Tamil_Nadu:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Tamil_Nadu = False


    screen.fill(bg_color)


    for row in range(len(maze)):
        for col in range(len(maze[0])):
            tile = pygame.Rect(col * tile_siZe, row * tile_siZe,tile_siZe, tile_siZe)

            a = col * tile_siZe + 20


            b = row * tile_siZe + 20


            if maze[row][col] == 0:
                screen.blit(path,tile)
                # pygame.draw.rect(screen,black,tile)
                # pygame.draw.rect(screen, 'white', tile, 2)
            if maze[row][col] == 1:
                screen.blit(wall,tile)
                # pygame.draw.rect(screen,red,tile)
                # pygame.draw.rect(screen,'white',tile,3)

            if maze[row][col]== 10:
                screen.blit(path,tile)
                screen.blit(ending,tile)
                # pygame.draw.rect(screen,'green',tile)
            if maze[row][col]== 20:
                pygame.draw.rect(screen, 'blue', tile)
                screen.blit(start,tile)

            if maze[row][col] == 50:
                screen.blit(path,tile)
                screen.blit(coins,tile)
                # pygame.draw.circle(screen,'yellow',(a,b),15)




    playerx = player_coloumn * tile_siZe + tile_siZe // 2
    playery = player_row * tile_siZe + tile_siZe // 2

    screen.blit(player,(playerx-25,playery-20 ))
    # pygame.draw.circle(screen, 'red', (playerx, playery), 15)
    # pygame.draw.circle(screen, '#1600f5', (playerx, playery), 15, 4)

    keys = pygame.key.get_pressed()
    row2, col2 = player_row,player_coloumn
    if keys[pygame.K_RIGHT]:
        col2 += 1

    if keys[pygame.K_LEFT]:
        col2 -= 1
    if keys[pygame.K_DOWN]:
        row2 += 1
    if keys[pygame.K_UP]:
        row2 -=  1




    # player_row = row2
    # player_coloumn  = col2
    if 0<= row2< len(maze) and 0<= col2< len(maze[0]):

        if maze[row2][col2]== 0 or maze[row2][col2]==50 or maze[row2][col2]==20 or maze[row2][col2]== 10:
           player_row,player_coloumn = row2,col2
           if maze[row2][col2]==50:
               maze[row2][col2]=0
               score += 1


    if  maze[row2][col2] == 10:
        Tamil_Nadu = False



    pygame.draw.rect(screen,'blue',(650,10,100,25))
    font = pygame.font.Font(None,25)
    text = font.render(f"Score:{score}",True,'white')

    screen.blit(text,(670,15))


    pygame.display.flip()
    pygame.time.delay(150)
