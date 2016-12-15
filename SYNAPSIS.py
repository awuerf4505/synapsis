# Imports
import pygame
import intersects

# Initialize game engine
pygame.init()


# Window
WIDTH = 1200
HEIGHT = 650
SIZE = (WIDTH, HEIGHT)
TITLE = "SYNAPSIS"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 120

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
PURPLE = (200, 0, 200)
BRAIN = (244, 180, 209)
# Fonts
MY_FONT = pygame.font.Font(None, 35)
MY_FONT2 = pygame.font.Font(None, 100)
myfont = pygame.font.SysFont("monospace", 55)

#img
test_image = pygame.image.load("brain.png") 
test_image2 = pygame.image.load("win_brain.png") 
test_image3 = pygame.image.load("sad_brain.png") 
test_image4 = pygame.image.load("sad_message.png") 

# Make a player
player =  [925, 600, 25, 25]
player_vx = 0
player_vy = 0
player_speed = 5

# Make enemy
enemy =  [305, 125, 25, 25]
enemy_vx = 0
enemy_vy = 0
enemy_speed = 5

#Make Walls
wall1 =  [300, 175, 25, 450]
wall2 =  [300, 275, 75, 25]
wall3 =  [350, 275, 25, 75]
wall4 =  [300, 375, 125, 25]
wall5 =  [400, 325, 25, 75]
wall6 =  [300, 425, 75, 25]
wall7 =  [300, 625, 600, 25]
wall8 =  [500, 375, 25, 275]
wall9 =  [400, 525, 125, 25]
wall10 =  [350, 475, 275, 25]
wall11 =  [350, 475, 25, 125]
wall12 =  [350, 575, 125, 25]
wall13 =  [550, 475, 25, 125]
wall14 =  [400, 425, 25, 75]
wall15 =  [400, 425, 75, 25]
wall16 =  [450, 275, 25, 175]
wall17 =  [400, 275, 75, 25]
wall18 =  [500, 375, 125, 25]
wall19 =  [600, 25, 25, 350]
wall20 =  [500, 325, 125, 25]
wall21 =  [500, 200, 25, 125]
wall22 =  [350, 200, 175, 50]
wall23 =  [600, 150, 75, 25]
wall24 =  [650, 100, 25, 175]
wall25 =  [650, 275, 75, 25]
wall26 =  [650, 100, 75, 25]
wall27 =  [700, 50, 25, 75]
wall28 =  [700, 50, 150, 25]
wall29 =  [300, 0, 625, 25]
wall30 =  [300, 0, 25, 100]
wall31 =  [300, 50, 75, 25]
wall32 =  [350, 50, 25, 75]
wall33 =  [350, 100, 75, 25]
wall34 =  [400, 0, 25, 75]
wall35 =  [400, 50, 75, 25]
wall36 =  [450, 50, 25, 125]
wall37 =  [350, 150, 225, 25]
wall38 =  [550, 50, 25, 250]
wall39 =  [500, 50, 75, 25]
wall40 =  [500, 50, 25, 75]
wall41 =  [650, 0, 25, 75]
wall42 =  [925, 0, 25, 575]
wall43 =  [875, 50, 75, 25]
wall44 =  [750, 100, 175, 25]
wall45 =  [850, 100, 25, 75]
wall46 =  [800, 150, 100, 25]
wall47 =  [750, 100, 25, 75]
wall48 =  [700, 150, 75, 25]
wall49 =  [700, 150, 25, 100]
wall50 =  [700, 150, 75, 25]
wall51 =  [750, 200, 25, 150]
wall52 =  [750, 275, 150, 25]
wall53 =  [800, 200, 150, 50]
wall54 =  [875, 525, 75, 25]
wall55 =  [875, 525, 25, 75]
wall56 =  [750, 575, 50, 75]
wall57 =  [600, 575, 175, 25]
wall58 =  [700, 425, 25, 175]
wall59 =  [600, 525, 125, 25]
wall60 =  [650, 475, 75, 25]
wall61 =  [550, 425, 250, 25]
wall62 =  [650, 375, 25, 75]
wall63 =  [825, 475, 25, 125]
wall64 =  [750, 525, 75, 25]
wall65 =  [750, 475, 50, 75]
wall66 =  [825, 475, 75, 25]
wall67 =  [875, 325, 25, 175]
wall68 =  [825, 425, 75, 25]
wall69 =  [825, 325, 75, 25]
wall70 =  [800, 325, 50, 75]
wall71 =  [700, 375, 125, 25]
wall72 =  [700, 325, 25, 75]
wall73 =  [650, 325, 75, 25]

walls = [wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14, wall15, wall16, wall17, wall18, wall19, wall20, wall21, wall22, wall23, wall24, wall25, wall26, wall27, wall28, wall29, wall30, wall31, wall32, wall33, wall34, wall35, wall36, wall37, wall38, wall39, wall40, wall41, wall42, wall43, wall44, wall45, wall46, wall47, wall48, wall49, wall50, wall51, wall52, wall53, wall54, wall55, wall56, wall57, wall58, wall59, wall60, wall61, wall62, wall63, wall64, wall65, wall66, wall67, wall68, wall69, wall70, wall71, wall72, wall73]


# stages
START = 0
PLAYING = 1
END = 2


def setup():
    global coins, stage, player, enemy, time_remaining, ticks, switch, red_doors, collidables, switch_two, purple_doors, collidables_two
    
    # Make coins
    coin1 = [350, 25, 25, 25]
    coin2 = [575, 75, 25, 25]
    coin3 = [900, 25, 25, 25]
    coin4 = [325, 225, 25, 25]
    coin5 = [875, 125, 25, 25]
    coin6 = [900, 250, 25, 25]
    coin7 = [525, 275, 25, 25]
    coin8 = [650, 300, 25, 25]
    coin9 = [850, 350, 25, 25]
    coin10 = [425, 400, 25, 25]
    coin11 = [525, 500, 25, 25]
    coin12 = [875, 500, 25, 25]
    coin13 = [475, 550, 25, 25]
    coin14 = [775, 550, 25, 25]


    coins = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14]
    player =  [925, 600, 25, 25]
    enemy =  [305, 125, 25, 25]

    switch = [625, 25, 25, 25]
    door1 = [350, 125, 25, 25]
    red_doors = [door1]
    collidables = walls + red_doors

    switch_two = [475, 500, 25, 25]
    door2 = [900, 450, 25, 25]
    door3 = [850, 550, 25, 25]
    purple_doors = [door2, door3]
    collidables_two = walls + purple_doors

    stage = START
    time_remaining = 60
    ticks = 0
    
# Game loop
setup()
win = False
done = False
score = 0
red_doors_open = False
purple_doors_open = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:     
             if stage == START:
                    if event.key == pygame.K_SPACE:
                        stage = PLAYING                  
             elif stage == END:
                    if win ==True:
                        if event.key == pygame.K_SPACE:
                            setup()
                    if win == False:
                        if event.key == pygame.K_SPACE:
                            setup()
    '''Key Functions'''
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
        #player
        if up:
            enemy_vy = -enemy_speed
        elif down:
            enemy_vy = enemy_speed
        else:
            enemy_vy = 0
        if left:
            enemy_vx = -enemy_speed
        elif right:
            enemy_vx = enemy_speed
        else:
             enemy_vx = 0

        #enemy
        if uptwo:
            player_vy = -player_speed
        elif downtwo:    
            player_vy = player_speed
        else:
            player_vy = 0        
        if lefttwo:
            player_vx = -player_speed
        elif righttwo:
            player_vx = player_speed
        else:
            player_vx = 0
        
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
    for c in collidables:
        if intersects.rect_rect(player, c):        
            if player_vx > 0:
                player[0] = c[0] - player[2]
            elif player_vx < 0:
                player[0] = c[0] + c[2]
        if intersects.rect_rect(enemy, c):        
            if enemy_vx > 0:
                enemy[0] = c[0] - enemy[2]
            elif enemy_vx < 0:
                enemy[0] = c[0] + c[2]
    for c in collidables_two:
        if intersects.rect_rect(player, c):        
            if player_vx > 0:
                player[0] = c[0] - player[2]
            elif player_vx < 0:
                player[0] = c[0] + c[2]
        if intersects.rect_rect(enemy, c):        
            if enemy_vx > 0:
                enemy[0] = c[0] - enemy[2]
            elif enemy_vx < 0:
                enemy[0] = c[0] + c[2]                
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
    for c in collidables:
        if intersects.rect_rect(player, c):                    
            if player_vy > 0:
                player[1] = c[1] - player[3]
            if player_vy < 0:
                player[1] = c[1] + c[3]
        if intersects.rect_rect(enemy, c):                    
            if player_vy > 0:
                enemy[1] = c[1] - enemy[3]
            if enemy_vy < 0:
                enemy[1] = c[1] + c[3]
    for c in collidables_two:
        if intersects.rect_rect(player, c):                    
            if player_vy > 0:
                player[1] = c[1] - player[3]
            if player_vy < 0:
                player[1] = c[1] + c[3]
        if intersects.rect_rect(enemy, c):                    
            if player_vy > 0:
                enemy[1] = c[1] - enemy[3]
            if enemy_vy < 0:
                enemy[1] = c[1] + c[3]                
    '''time/ticks'''
    if stage == PLAYING:
        ticks += 1

        if ticks % refresh_rate == 0:
            time_remaining -= 1

        if time_remaining == 0:
            stage = END

    '''screen edge detection'''
    if stage == PLAYING:
         if player[0] < 0 or player[0] > 1200 or \
           player[1] < 0 or player[1] > 650:
            stage = END
    if stage == PLAYING:
         if enemy[0] < 0 or enemy[0] > 1200 or \
           enemy[1] < 0 or enemy[1] > 650:
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
        
    ''' open red door on switch contact '''
    if intersects.rect_rect(player, switch):
        red_doors_open = True
        collidables = [c for c in collidables if c not in red_doors]

    ''' open purple door on switch contact '''
    if intersects.rect_rect(enemy, switch_two):
        purple_doors_open = True

        collidables_two = [c for c in collidables_two if c not in purple_doors]        
    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    '''background'''
    if stage == START:
        screen.fill(WHITE)
       
    if stage == PLAYING:
        screen.fill(BLACK)
        '''player and enemy'''
        pygame.draw.rect(screen, WHITE, player)
        pygame.draw.rect(screen, GREY, enemy)

        '''walls'''
        for w in walls:
            pygame.draw.rect(screen, BRAIN, w)


        '''coins'''
        for c in coins:
            pygame.draw.rect(screen, BLUE, c)
        
        '''switches and doors'''
        pygame.draw.rect(screen, GREEN, switch)
        pygame.draw.rect(screen, GREEN, switch_two)

        if not red_doors_open:
            for d in red_doors:
                pygame.draw.rect(screen, RED, d)
        if not purple_doors_open:
            for d in purple_doors:
                pygame.draw.rect(screen, PURPLE, d)
            
        ''' timer text '''
        timer_text = MY_FONT.render(str(time_remaining), True, WHITE)
        screen.blit(timer_text, [175, 250])

    '''font in stages'''
    if stage == START:
        text1 = myfont.render("SYNAPSIS", True, BLACK)
        text2 = MY_FONT.render("Press SPACE to play.", True, BLACK)
        screen.blit(text1, [483, 150])
        screen.blit(text2, [495, 200])
        screen.blit(test_image, (565,250)) 

    elif stage == END:
        if win == True:
            screen.fill(WHITE)
            text1 = MY_FONT2.render("YAY", True, BLACK)
            text2 = MY_FONT2.render("YOU WON!!!", True, BLACK)
            text3 = MY_FONT2.render("Press SPACE for Level 2.", True, BLACK)
            screen.blit(text1, [550, 100])
            screen.blit(text2, [425, 175])
            screen.blit(text3, [225, 250])
            screen.blit(test_image2, (500,325)) 

        if win == False:
            screen.fill(WHITE)
            text1 = MY_FONT2.render("DANG", True, BLACK)
            text2 = MY_FONT.render("Your Score Was: " + str(score) + "/14", True, BLACK)
            text3 = MY_FONT2.render("Press SPACE to restart.", True, BLACK)
            screen.blit(text1, [475, 150])
            screen.blit(text2, [455, 225])
            screen.blit(text3, [225, 250])
            screen.blit(test_image3, (500,350)) 
            screen.blit(test_image4, (642,350)) 

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()




