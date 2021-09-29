import pygame
#########################
#기본 초기화(반드시 해야함)
pygame.init()

screen_width=480
screen_height=640
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("me")

clock = pygame.time.Clock()
########################


#1.사용자 게임 초기화

#게임 이름 설정
background= pygame.image.load("C:\\Users\\수빈-J\\Desktop\\PythonWorkspace\\pygame_basic\\bae.png")

character =pygame.image.load("C:\\Users\\수빈-J\\Desktop\\PythonWorkspace\\pygame_basic\\cha.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2)-(character_width/2)
character_y_pos = screen_height-character_height

to_x=0
to_y=0

character_speed=0.6

enemy =pygame.image.load("C:\\Users\\수빈-J\\Desktop\\PythonWorkspace\\pygame_basic\\ene.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width/2)-(enemy_width/2)
enemy_y_pos = (screen_height/2)-(enemy_height/2)

game_font = pygame.font.Font(None, 40)

total_time =10

start_ticks = pygame.time.get_ticks()


running=True
while running:
    dt = clock.tick(60)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_LEFT:
                to_x -= character_speed
            elif event.key ==pygame.K_RIGHT:
                to_x += character_speed
            elif event.key ==pygame.K_UP:
                to_y -= character_speed
            elif event.key ==pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                to_x =0
            elif event.key == pygame.K_UP or event.key ==pygame.K_DOWN:
                to_y =0
    character_x_pos += to_x *dt
    character_y_pos +=to_y*dt

    if character_x_pos <0 :
            character_x_pos=0
    elif character_x_pos >screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    if character_y_pos<0:
        character_y_pos=0
    elif character_y_pos>screen_height-character_height:
        character_y_pos=screen_height-character_height

    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running =False

    screen.blit(background, (0,0))

    screen.blit(character,(character_x_pos,character_y_pos))

    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks()-start_ticks)/1000

    timer = game_font.render(str(int(total_time-elapsed_time)),True,(255,255,255))

    screen.blit(timer,(10,10))

    if total_time-elapsed_time <=0:
            print("time out")
            running = False

    pygame.display.update()

pygame.time.delay(2000)

pygame.quit()