import pygame
import random
import os

pygame.mixer.init()
pygame.init()


# colors
white= (255,255,255)
red= (255,0,0)
black= (0,0,0)
blue=(50,153,213)
yellow=(255,255,102)
green=(0,255,0)

# Creating window
screen_width=900
screen_height=600
gameWindow=pygame.display.set_mode((screen_width, screen_height))


# Game title
pygame.display.set_caption("My First Game - Snakes")
pygame.display.update()


clock=pygame.time.Clock()
font=pygame.font.SysFont(None, 55)

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    gameWindow.blit(screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list ,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size ])

def welcome():
    exit_game=False
    while exit_game==False:
        # gameWindow.fill((220,200,200))
        # text_screen("Welcome to Snakes", black, 250,250)
        
        # Background image
        bgimg=pygame.image.load("home_picture.jpg")
        bgimg=pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

        gameWindow.blit(bgimg, (0,0))
        text_screen("Press Space Bar To Play", black, 230,80)


        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    pygame.mixer.music.load("background.mp3")
                    pygame.mixer.music.play()
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(50)


# Creating a game loop
def gameloop():

    # Game specific variables
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    food_x=random.randint(20, int(screen_width/2))
    food_y=random.randint(20,int(screen_height/2))
    snake_size=14
    fps=50
    radius=7
    score=0
    init_velocity=4.5
    snk_list=[]
    snk_len=1

    # Check if hiscore file exists
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt","w") as f:
            f.write("0")

    with open("hiscore.txt","r") as f:
        hiscore=f.read()

    while exit_game==False:
        if game_over==True:
            with open("hiscore.txt","w") as f:
                f.write(str(hiscore))

            # gameWindow.fill(blue)
            goimg=pygame.image.load("game_over_picture.jpg")
            goimg=pygame.transform.scale(goimg, (screen_width, screen_height)).convert_alpha()
            gameWindow.blit(goimg, (0,0))
            text_screen("Score: " + str(score) + "   High Score: " + str(hiscore), white , 220,400)
            text_screen("Press Enter To Continue", white, 227,470)


            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                    
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    
                    if event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RIGHT:
                            velocity_x=init_velocity
                            velocity_y=0

                        if event.key==pygame.K_LEFT:
                            velocity_x=-init_velocity
                            velocity_y=0

                        if event.key==pygame.K_UP:
                            velocity_y=-init_velocity
                            velocity_x=0

                        if event.key==pygame.K_DOWN:
                            velocity_y=init_velocity
                            velocity_x=0

                        if event.key==pygame.K_q:
                            score+=10
                            snk_len+=5
                            food_x=random.randint(20, int(screen_width/2))
                            food_y=random.randint(20,int(screen_height/2))

                        if score>int(hiscore):
                            hiscore=score

            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10 :
                score+=10
                food_x=random.randint(20, int(screen_width/2))
                food_y=random.randint(20,int(screen_height/2))
                snk_len+=5
                if score>int(hiscore):
                    hiscore=score

                


            gameWindow.fill(blue)
            text_screen("Score: " + str(score) + "   High Score: " + str(hiscore), red , 5,5)
            # gameWindow.blit(bgimg, (0,0))

            pygame.draw.circle(gameWindow, yellow, [food_x, food_y], radius )

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)>snk_len:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over=True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over=True
                pygame.mixer.music.load("game_over.mp3")
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snk_list, snake_size)
            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size ])
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()
welcome()




'''QUIT              none
ACTIVEEVENT       gain, state
KEYDOWN           key, mod, unicode, scancode
KEYUP             key, mod, unicode, scancode
MOUSEMOTION       pos, rel, buttons, touch
MOUSEBUTTONUP     pos, button, touch
MOUSEBUTTONDOWN   pos, button, touch
JOYAXISMOTION     joy (deprecated), instance_id, axis, value
JOYBALLMOTION     joy (deprecated), instance_id, ball, rel
JOYHATMOTION      joy (deprecated), instance_id, hat, value
JOYBUTTONUP       joy (deprecated), instance_id, button
JOYBUTTONDOWN     joy (deprecated), instance_id, button
VIDEORESIZE       size, w, h
VIDEOEXPOSE       none
USEREVENT         code'''