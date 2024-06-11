import pygame
import random
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
x = pygame.init()
width_of_screen = 500
height_of_screen = 500
gameWindow = pygame.display.set_mode((width_of_screen,height_of_screen))
pygame.display.set_caption("snake game")
pygame.display.update()
clock = pygame.time.Clock()

# Load the images
background_img = pygame.image.load('background.jpg')
background_img = pygame.transform.scale(background_img, (width_of_screen, height_of_screen))
welcome_img = pygame.image.load('welcome.jpg')
welcome_img = pygame.transform.scale(welcome_img, (width_of_screen, height_of_screen))
game_over_img = pygame.image.load('game_over.jpg')
game_over_img = pygame.transform.scale(game_over_img, (width_of_screen, height_of_screen))

# plotting the snake
def plot_snake(gameWindow, color,snake_list,snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow,color,[x,y,snake_size,snake_size])

# making the welcome screen
def welcome():
    game_exit = False
    while not game_exit:
        gameWindow.blit(background_img, (0, 0))  # Display the background image
        gameWindow.blit(welcome_img, (0, 0))  # Display the welcome image
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_exit = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game()
        pygame.display.update()
        clock.tick(60)

#snake game 
def game():
    game_exit= False
    game_over= False
    snake_x=45
    snake_y=55
    velocity_x= 0
    velocity_y= 0
    init_velocity = 7
    score= 0
    apple_x = random.randint(20,width_of_screen/2)
    apple_y = random.randint(20,height_of_screen/2)
    snake_size=30
    snake_list = []
    snake_length = 1
    fps=40
    while not game_exit:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(game_over_img, (0, 0))  # Display the game over image
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type== pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =  init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y =  init_velocity
                        velocity_x = 0
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x - apple_x)<20 and abs(snake_y - apple_y)<20:
                score+=10
                apple_x = random.randint(20,width_of_screen/2)
                apple_y = random.randint(20,height_of_screen/2)
                snake_length+=5
            gameWindow.blit(background_img, (0, 0))  # Display the background image
            pygame.draw.rect(gameWindow,red,[apple_x,apple_y,snake_size,snake_size])
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
            if snake_x<0 or snake_x>width_of_screen or snake_y<0 or snake_y>height_of_screen:
                game_over = True
            plot_snake(gameWindow,black,snake_list,snake_size)
            pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
        pygame.display.update() 
        clock.tick(fps)
    pygame.quit()
    quit()

welcome()
