# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "Maze"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)

# Fonts
MY_FONT = pygame.font.Font(None, 35)

# Make a player
player =  [625, 600, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# Make enemy
enemy =  [5, 125, 25, 25]
enemy_vx = 0
enemy_vy = 0
enemy_speed = 5

#Make Walls
wall1 =  [0, 175, 25, 450]
wall2 =  [0, 275, 75, 25]
wall3 =  [50, 275, 25, 75]
wall4 =  [0, 375, 125, 25]
wall5 =  [100, 325, 25, 75]
wall6 =  [0, 425, 75, 25]
wall7 =  [0, 625, 600, 25]
wall8 =  [200, 375, 25, 275]
wall9 =  [100, 525, 125, 25]
wall10 =  [50, 475, 275, 25]
wall11 =  [50, 475, 25, 125]
wall12 =  [50, 575, 125, 25]
wall13 =  [250, 475, 25, 125]
wall14 =  [100, 425, 25, 75]
wall15 =  [100, 425, 75, 25]
wall16 =  [150, 275, 25, 175]
wall17 =  [100, 275, 75, 25]
wall18 =  [200, 375, 125, 25]
wall19 =  [300, 50, 25, 325]
wall20 =  [200, 325, 125, 25]
wall21 =  [200, 200, 25, 125]
wall22 =  [50, 200, 175, 50]
wall23 =  [300, 150, 75, 25]
wall24 =  [350, 100, 25, 175]
wall25 =  [350, 275, 75, 25]
wall26 =  [350, 100, 75, 25]
wall27 =  [400, 50, 25, 75]
wall28 =  [400, 50, 150, 25]
wall29 =  [0, 0, 625, 25]
wall30 =  [0, 0, 25, 100]
wall31 =  [0, 50, 75, 25]
wall32 =  [50, 50, 25, 75]
wall33 =  [50, 100, 75, 25]
wall34 =  [100, 0, 25, 75]
wall35 =  [100, 50, 75, 25]
wall36 =  [150, 50, 25, 125]
wall37 =  [50, 150, 225, 25]
wall38 =  [250, 50, 25, 250]
wall39 =  [200, 50, 75, 25]
wall40 =  [200, 50, 25, 75]
wall41 =  [350, 0, 25, 75]
wall42 =  [625, 0, 25, 575]
wall43 =  [575, 50, 75, 25]
wall44 =  [450, 100, 175, 25]
wall45 =  [550, 100, 25, 75]
wall46 =  [500, 150, 100, 25]
wall47 =  [450, 100, 25, 75]
wall48 =  [400, 150, 75, 25]
wall49 =  [400, 150, 25, 100]
wall50 =  [400, 150, 75, 25]
wall51 =  [450, 200, 25, 150]
wall52 =  [450, 275, 150, 25]
wall53 =  [500, 200, 150, 50]
wall54 =  [575, 525, 75, 25]
wall55 =  [575, 525, 25, 75]
wall56 =  [450, 575, 50, 75]
wall57 =  [300, 575, 175, 25]
wall58 =  [400, 425, 25, 175]
wall59 =  [300, 525, 125, 25]
wall60 =  [350, 475, 75, 25]
wall61 =  [250, 425, 250, 25]
wall62 =  [350, 375, 25, 75]
wall63 =  [525, 475, 25, 125]
wall64 =  [450, 525, 75, 25]
wall65 =  [450, 475, 50, 75]
wall66 =  [525, 475, 75, 25]
wall67 =  [575, 325, 25, 175]
wall68 =  [525, 425, 75, 25]
wall69 =  [525, 325, 75, 25]
wall70 =  [500, 325, 50, 75]
wall71 =  [400, 375, 125, 25]
wall72 =  [400, 325, 25, 75]
wall73 =  [350, 325, 75, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58, wall59, wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73]


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global coins, stage, player, time_remaining, ticks
    
    # Make coins
    coin1 = [50, 25, 25, 25]
    coin2 = [275, 75, 25, 25]
    coin3 = [600, 25, 25, 25]
    coin4 = [25, 225, 25, 25]
    coin5 = [575, 125, 25, 25]
    coin6 = [600, 250, 25, 25]
    coin7 = [225, 275, 25, 25]
    coin8 = [350, 300, 25, 25]
    coin9 = [550, 350, 25, 25]
    coin10 = [125, 400, 25, 25]
    coin11 = [225, 500, 25, 25]
    coin12 = [575, 500, 25, 25]
    coin13 = [175, 550, 25, 25]
    coin14 = [375, 550, 25, 25]


    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14]
    player =  [625, 600, 25, 25]
    enemy =  [5, 125, 25, 25]


    
    stage = START
    time_remaining = 120
    ticks = 0
# Game loop
setup()
win = False
done = False
score = 0

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            
             if stage == START:
                    if event.key == pygame.K_SPACE:
                        stage = PLAYING
                  
             elif stage == END:
                    if event.key == pygame.K_SPACE:
                        setup()

    if stage == PLAYING:
        pressed = pygame.key.get_pressed()

        up = pressed[pygame.K_UP]
        down = pressed[pygame.K_DOWN]
        left = pressed[pygame.K_LEFT]
        right = pressed[pygame.K_RIGHT]
        space = pressed[pygame.K_SPACE]
        uptwo = pressed[pygame.K_w]
        downtwo = pressed[pygame.K_s]
        lefttwo = pressed[pygame.K_a]
        righttwo = pressed[pygame.K_d]  

        if up:
            player_vy = -player_speed
        elif down:
            player_vy = player_speed
        else:
            player_vy = 0
        
        if left:
            player_vx = -player_speed
        elif right:
            player_vx = player_speed
        else:
             player_vx = 0


        if uptwo:
            enemy_vy = -enemy_speed
        elif downtwo:    
            enemy_vy = enemy_speed
        else:
            enemy_vy = 0        
        if lefttwo:
            enemy_vx = -enemy_speed
        elif righttwo:
            enemy_vx = enemy_speed
        else:
            enemy_vx = 0
        
    # Game logic (Check for collisions, update points, etc.)
    ''' move the player in horizontal direction '''
    if stage == PLAYING:
        player[0] += player_vx
        enemy[0] += enemy_vx

    ''' resolve collisions horizontally '''
    for w in walls:
        if intersects.rect_rect(player, w):        
            if player_vx > 0:
                player[0] = w[0] - player[2]
            elif player_vx < 0:
                player[0] = w[0] + w[2]
        if intersects.rect_rect(enemy, w):        
            if enemy_vx > 0:
                enemy[0] = w[0] - enemy[2]
            elif enemy_vx < 0:
                enemy[0] = w[0] + w[2]
    ''' move the player in vertical direction '''
    player[1] += player_vy
    enemy[1] += enemy_vy

    ''' resolve collisions vertically '''
    for w in walls:
        if intersects.rect_rect(player, w):                    
            if player_vy > 0:
                player[1] = w[1] - player[3]
            if player_vy < 0:
                player[1] = w[1] + w[3]
        if intersects.rect_rect(enemy, w):                    
            if enemy_vy > 0:
                enemy[1] = w[1] - enemy[3]
            if enemy_vy < 0:
                enemy[1] = w[1] + w[3]    

    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END

    if stage == PLAYING:
         if player[0] < 0 or player[0] > 1200 or \
           player[1] < 0 or player[1] > 800:
            stage = END
    if stage == PLAYING:
         if enemy[0] < 0 or enemy[0] > 1200 or \
           enemy[1] < 0 or enemy[1] > 800:
            stage = END


    ''' get the coins '''
    #coins = [c for c in coins if not intersects.rect_rect(player, c)]

    hit_list = [c for c in coins if intersects.rect_rect(player, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score += 1
        print("sound!")

    hit_list = [c for c in coins if intersects.rect_rect(enemy, c)]
    
    for hit in hit_list:
        coins.remove(hit)
        score += 1
        print("sound!")        

    if len(coins) == 0:
        win = True
        stage = END
        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, GREY, enemy)

    for w in walls:
        pygame.draw.rect(screen, BLUE, w)

    for c in coins:
        pygame.draw.rect(screen, YELLOW, c)
        
    ''' timer text '''
    timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
    screen.blit(timer_text, [50, 50])

    if stage == START:
        text1 = MY_FONT.render("Block Maze", True, WHITE)
        text2 = MY_FONT.render("(Press SPACE to play.)", True, WHITE)
        screen.blit(text1, [675, 150])
        screen.blit(text2, [675, 200])
    elif stage == END:
        text1 = MY_FONT.render("Game Over", True, WHITE)
        text2 = MY_FONT.render("(Your Score Was: " + str(score) + ". Press SPACE to restart.)", True, WHITE)
        screen.blit(text1, [675, 150])
        screen.blit(text2, [675, 200])


    
    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()




